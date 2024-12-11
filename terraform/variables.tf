variable "subscription_id" {
  type = string
}

variable "tenant_id" {
  type = string
}

variable "client_id" {
  type = string
}

variable "client_secret" {
  type = string
}

variable "vm_name" {
  type = string
}

variable "owner_email" {
  type = string
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "vm_size" {
  type    = string
  default = "Standard_DS1_v2"
}

variable "publisher" {
  type    = string
  default = "Canonical"
}

variable "offer" {
  type    = string
  default = "UbuntuServer"
}

variable "sku" {
  type    = string
  default = "18.04-LTS"
}

variable "version" {
  type    = string
  default = "latest"
}