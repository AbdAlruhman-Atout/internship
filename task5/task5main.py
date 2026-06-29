from contacts import (
    add_contact,
    remove_contact,
    search_by_name,
    load_contacts,
    save_contacts,
    format_contact,
)

FILEPATH = "contacts.json"


def list_contacts(contacts):
    for name, details in contacts.items():
        print(format_contact(name, details))


def main():
    contacts = load_contacts(FILEPATH)

    try:
        while True:
            print("\n1. Add")
            print("2. Remove")
            print("3. Search")
            print("4. List")
            print("5. Quit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                city = input("City: ")

                add_contact(
                    contacts,
                    name,
                    phone=phone,
                    email=email,
                    city=city,
                )
                save_contacts(contacts, FILEPATH)
                print("Contact added.")

            elif choice == "2":
                name = input("Name to remove: ")
                remove_contact(contacts, name)
                save_contacts(contacts, FILEPATH)
                print("Contact removed.")

            elif choice == "3":
                query = input("Search name: ")
                results = search_by_name(contacts, query)

                for name, details in results:
                    print(format_contact(name, details))

            elif choice == "4":
                list_contacts(contacts)

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

    except Exception as error:
        print(f"Something went wrong: {error}")

    finally:
        print("Goodbye!")


if __name__ == "__main__":
    main()
