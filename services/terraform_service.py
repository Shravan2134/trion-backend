"""Service for managing Terraform operations."""

import json
import subprocess
from typing import Dict, Optional
from pathlib import Path

class TerraformService:
    def __init__(self, working_dir: str):
        self.working_dir = Path(working_dir)

    def create_tfvars(self, variables: Dict[str, str]) -> str:
        """Create terraform.tfvars file with the provided variables."""
        tfvars_path = self.working_dir / "terraform.tfvars.json"
        with open(tfvars_path, 'w') as f:
            json.dump(variables, f, indent=2)
        return str(tfvars_path)

    def init(self) -> subprocess.CompletedProcess:
        """Initialize Terraform working directory."""
        return subprocess.run(
            ['terraform', 'init'],
            cwd=self.working_dir,
            capture_output=True,
            text=True,
            check=True
        )

    def apply(self, auto_approve: bool = True) -> subprocess.CompletedProcess:
        """Apply Terraform configuration."""
        cmd = ['terraform', 'apply']
        if auto_approve:
            cmd.append('-auto-approve')
        
        return subprocess.run(
            cmd,
            cwd=self.working_dir,
            capture_output=True,
            text=True,
            check=True
        )

    def destroy(self, auto_approve: bool = True) -> subprocess.CompletedProcess:
        """Destroy Terraform-managed infrastructure."""
        cmd = ['terraform', 'destroy']
        if auto_approve:
            cmd.append('-auto-approve')
        
        return subprocess.run(
            cmd,
            cwd=self.working_dir,
            capture_output=True,
            text=True,
            check=True
        )