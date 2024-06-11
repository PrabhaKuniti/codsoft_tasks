CONTACTS_FILE = 'contacts.txt'

def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                name, phone, email, address = line.strip().split('|')
                contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']}|{contact['phone']}|{contact['email']}|{contact['address']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact for {name} added successfully.")

def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("\nNo contacts found.")

def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("Leave the field blank if you don't want to change it.")
            phone = input(f"Enter new phone number (current: {contact['phone']}): ")
            email = input(f"Enter new email (current: {contact['email']}): ")
            address = input(f"Enter new address (current: {contact['address']}): ")
            
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
                
            save_contacts(contacts)
            print(f"Contact for {name} updated successfully.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact for {name} deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    print("Welcome to the Contact Book Application!")
    main()
