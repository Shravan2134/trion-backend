"""Azure configuration settings."""

AZURE_CREDENTIALS = {
    "subscription_id": "your-subscription-id",
    "tenant_id": "your-tenant-id",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret"
}

# VM Configuration defaults
DEFAULT_VM_CONFIG = {
    "location": "eastus",
    "vm_size": "Standard_DS1_v2",
    "publisher": "Canonical",
    "offer": "UbuntuServer",
    "sku": "18.04-LTS",
    "version": "latest"
}