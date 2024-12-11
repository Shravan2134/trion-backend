terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
  tenant_id       = var.tenant_id
  client_id       = var.client_id
  client_secret   = var.client_secret
}

resource "azurerm_resource_group" "vm_rg" {
  name     = "${var.vm_name}-rg"
  location = var.location
}

resource "azurerm_virtual_network" "vm_network" {
  name                = "${var.vm_name}-network"
  address_space       = ["10.0.0.0/16"]
  location           = azurerm_resource_group.vm_rg.location
  resource_group_name = azurerm_resource_group.vm_rg.name
}

resource "azurerm_subnet" "vm_subnet" {
  name                 = "${var.vm_name}-subnet"
  resource_group_name  = azurerm_resource_group.vm_rg.name
  virtual_network_name = azurerm_virtual_network.vm_network.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_network_interface" "vm_nic" {
  name                = "${var.vm_name}-nic"
  location           = azurerm_resource_group.vm_rg.location
  resource_group_name = azurerm_resource_group.vm_rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.vm_subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_virtual_machine" "main" {
  name                  = var.vm_name
  location             = azurerm_resource_group.vm_rg.location
  resource_group_name  = azurerm_resource_group.vm_rg.name
  network_interface_ids = [azurerm_network_interface.vm_nic.id]
  vm_size              = var.vm_size

  storage_image_reference {
    publisher = var.publisher
    offer     = var.offer
    sku       = var.sku
    version   = var.version
  }

  storage_os_disk {
    name              = "${var.vm_name}-osdisk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  os_profile {
    computer_name  = var.vm_name
    admin_username = "azureuser"
    admin_password = "Password1234!"  # In production, use a secure password management system
  }

  os_profile_linux_config {
    disable_password_authentication = false
  }

  tags = {
    environment = "production"
    owner_email = var.owner_email
  }
}