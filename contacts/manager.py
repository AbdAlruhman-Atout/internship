# Default argument values are evaluated once when the function is defined.
# This matters because mutable defaults like [] or {} can accidentally be shared between calls.
DEFAULT_CITY = "Unknown"


def add_contact(contacts, name, *, phone, email, city=DEFAULT_CITY):
    if name in contacts:
        raise ValueError(f"Contact '{name}' already exists.")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city,
    }


def remove_contact(contacts, name):
    if name not in contacts:
        raise KeyError(f"Contact '{name}' not found.")

    del contacts[name]


def update_contact(contacts, name, **fields):
    if name not in contacts:
        raise KeyError(f"Contact '{name}' not found.")

    contacts[name].update(fields)


def search_by_name(contacts, query):
    return [
        (name, details)
        for name, details in contacts.items()
        if query.lower() in name.lower()
    ]


def search_by_phone(contacts, phone):
    for name, details in contacts.items():
        if details["phone"] == phone:
            return name, details

    return None


def get_summary(contacts):
    total = len(contacts)
    cities = {details["city"] for details in contacts.values()}

    if len(cities) == 0:
        avg_per_city = 0
    else:
        avg_per_city = round(total / len(cities), 2)

    return total, cities, avg_per_city
