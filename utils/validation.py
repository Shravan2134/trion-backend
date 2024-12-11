"""Input validation utilities."""

import re

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_vm_name(name: str) -> bool:
    """Validate VM name according to Azure naming rules."""
    # Azure VM names must be 1-64 characters long and can only contain
    # letters, numbers, and hyphens (cannot start or end with hyphen)
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-]{0,62}[a-zA-Z0-9]$'
    return bool(re.match(pattern, name))