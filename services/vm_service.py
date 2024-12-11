"""Service for managing Azure VM operations."""

from typing import Dict, Optional
from utils.validation import validate_email, validate_vm_name
from config.azure_config import AZURE_CREDENTIALS, DEFAULT_VM_CONFIG
from services.terraform_service import TerraformService
import os

class VMService:
    def __init__(self):
        self.terraform = TerraformService("terraform")

    def create_vm(self, vm_name: str, owner_email: str) -> Dict[str, str]:
        """Create a new Azure VM with the specified parameters."""
        # Validate inputs
        if not validate_vm_name(vm_name):
            raise ValueError("Invalid VM name")
        if not validate_email(owner_email):
            raise ValueError("Invalid email address")

        # Prepare variables for Terraform
        variables = {
            **AZURE_CREDENTIALS,
            **DEFAULT_VM_CONFIG,
            "vm_name": vm_name,
            "owner_email": owner_email
        }

        # Create tfvars file
        self.terraform.create_tfvars(variables)

        # Initialize and apply Terraform configuration
        self.terraform.init()
        result = self.terraform.apply()

        if result.returncode != 0:
            raise Exception(f"Failed to create VM: {result.stderr}")

        return {
            "vm_name": vm_name,
            "owner_email": owner_email,
            "status": "created",
            "location": DEFAULT_VM_CONFIG["location"]
        }