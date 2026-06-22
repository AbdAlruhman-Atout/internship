contacts = {
    "Alice Johnson": {
        "phone": "059-1234567",
        "email": "alice@example.com",
        "city": "Nablus",
    },
    "Bob Smith": {
        "phone": "052-7654321",
        "email": "bob@example.com",
        "city": "Ramallah",
    },
}


def add_contact(contacts, name, phone, email, city):
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
    results = []

    for name, details in contacts.items():
        if query.lower() in name.lower():
            results.append((name, details))

    return results


def search_by_phone(contacts, phone):
    for name, details in contacts.items():
        if details["phone"] == phone:
            return name, details

    return None


def list_all(contacts):
    return sorted(contacts.items())


def get_cities(contacts):
    return {details["city"] for details in contacts.values()}


def contacts_in_cities(contacts, city_a, city_b):
    city_a_names = {
        name for name, details in contacts.items() if details["city"] == city_a
    }

    city_b_names = {
        name for name, details in contacts.items() if details["city"] == city_b
    }

    return {
        "union": city_a_names | city_b_names,
        "intersection": city_a_names & city_b_names,
    }


def get_recent(contacts, n=3):
    recent_contacts = list(contacts.items())[-n:]

    return [(name, details["phone"]) for name, details in recent_contacts]


# Complexity Analysis
# -------------------

# add_contact      → O(1)
# reason: Dictionary lookup and insertion are average-case constant time.

# remove_contact   → O(1)
# reason: Dictionary lookup and deletion are average-case constant time.

# search_by_name   → O(n)
# reason: Every contact name may need to be checked for a match.

# search_by_phone  → O(n)
# reason: Phone numbers are stored in nested dictionaries, so all contacts may need to be scanned.

# get_cities       → O(n)
# reason: Every contact must be visited to collect the set of unique cities.
