import json


def load_contacts(filepath):
    try:
        with open(filepath, "r") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return {}


def save_contacts(contacts, filepath):
    with open(filepath, "w") as file:
        json.dump(contacts, file, indent=2)
        return


def format_contact(name, details):
    return (
        f"{name} | "
        f"Phone: {details['phone']} | "
        f"Email: {details['email']} | "
        f"City: {details['city']}"
    )
