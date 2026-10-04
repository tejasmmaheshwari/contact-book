import json
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "contacts.json")


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")

    while True:
        phone = input("Enter phone number: ")

        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Please enter a valid 10-digit phone number.")

    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n===== CONTACTS =====")

    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("--------------------")


def search_contact(contacts):
    search_name = input("Enter the name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("\nContact found!")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    search_name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():

            print("\nContact found!")
            print(f"Current Name: {contact['name']}")
            print(f"Current Phone: {contact['phone']}")
            print(f"Current Email: {contact['email']}")

            new_name = input("Enter new name: ")

            while True:
                new_phone = input("Enter new phone number: ")

                if new_phone.isdigit() and len(new_phone) == 10:
                    break
                else:
                    print("Please enter a valid 10-digit phone number.")

            new_email = input("Enter new email: ")

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email

            save_contacts(contacts)

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact(contacts):
    search_name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():

            print("\nContact found!")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

            confirmation = input(
                "Are you sure you want to delete this contact? (yes/no): "
            )

            if confirmation.lower() == "yes":
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully!")
            else:
                print("Contact was not deleted.")

            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()