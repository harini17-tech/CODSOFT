contacts = {}
def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    contacts[name] = [email, phone, address]
    print("Contact Added!")
def view_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"\nName: {name}\nEmail: {info[0]}\nPhone: {info[1]}\nAddress: {info[2]}")
    else:
        print("No contacts found.")
def search_contact():
    name = input("Search Name: ")
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}\nEmail: {info[0]}\nPhone: {info[1]}\nAddress: {info[2]}")
    else:
        print("Contact not found.")
def delete_contact():
    name = input("Delete Name: ")
    if name in contacts:
        del contacts[name]
        print("Contact Deleted!")
    else:
        print("Contact not found.")
while True:
    print("\n1.Add  2.View  3.Search  4.Delete  5.Exit")
    choice = input("Choose: ")
    if choice == '1': add_contact()
    elif choice == '2': view_contacts()
    elif choice == '3': search_contact()
    elif choice == '4': delete_contact()
    elif choice == '5':
        print(" Thank you!")
        break
    else:
        print("Invalid choice!")
