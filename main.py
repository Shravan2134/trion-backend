"""Main application entry point."""

from services.vm_service import VMService

def main():
    vm_service = VMService()

    print("Azure VM Creation Utility")
    print("-" * 30)

    # Get user input
    vm_name = input("Enter VM name: ")
    owner_email = input("Enter owner email: ")

    try:
        # Create the VM
        result = vm_service.create_vm(vm_name, owner_email)
        print("\nVM created successfully!")
        print(f"VM Name: {result['vm_name']}")
        print(f"Location: {result['location']}")
        print(f"Owner Email: {result['owner_email']}")
        print(f"Status: {result['status']}")

    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()