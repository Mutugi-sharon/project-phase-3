from donations import add_donation, view_donations, delete_donation, update_donation

def main_menu():
    while True:
        print("\nMoesha Fundraising Management")
        print("1. Add a Donation")
        print("2. View Donations")
        print("3. Delete a Donation")
        print("4. Update a Donation")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_donation()
        elif choice == '2':
            view_donations()
        elif choice == '3':
            delete_donation()
        elif choice == '4':
            update_donation()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please choose a valid option.\n")

if __name__ == '__main__':
    main_menu()
