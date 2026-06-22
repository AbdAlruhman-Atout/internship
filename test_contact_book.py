import pytest
from contact_book import *


def sample_contacts():
    return {
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
        "Carol White": {
            "phone": "053-1111111",
            "email": "carol@example.com",
            "city": "Nablus",
        },
    }


def test_add_contact():
    contacts = sample_contacts()

    add_contact(
        contacts,
        "David Brown",
        "054-2222222",
        "david@example.com",
        "Hebron",
    )

    assert "David Brown" in contacts
    assert contacts["David Brown"]["phone"] == "054-2222222"


def test_add_duplicate_raises():
    contacts = sample_contacts()

    with pytest.raises(ValueError):
        add_contact(
            contacts,
            "Alice Johnson",
            "059-9999999",
            "alice2@example.com",
            "Jenin",
        )


def test_remove_contact():
    contacts = sample_contacts()

    remove_contact(contacts, "Bob Smith")

    assert "Bob Smith" not in contacts


def test_remove_missing_raises():
    contacts = sample_contacts()

    with pytest.raises(KeyError):
        remove_contact(contacts, "Unknown Person")


def test_update_contact():
    contacts = sample_contacts()

    update_contact(contacts, "Alice Johnson", city="Hebron")

    assert contacts["Alice Johnson"]["city"] == "Hebron"


def test_update_missing_raises():
    contacts = sample_contacts()

    with pytest.raises(KeyError):
        update_contact(contacts, "Unknown Person", city="Hebron")


def test_search_by_name_found():
    contacts = sample_contacts()

    result = search_by_name(contacts, "alice")

    assert len(result) == 1
    assert result[0][0] == "Alice Johnson"


def test_search_by_name_not_found():
    contacts = sample_contacts()

    result = search_by_name(contacts, "xyz")

    assert result == []


def test_search_by_phone_found():
    contacts = sample_contacts()

    result = search_by_phone(contacts, "052-7654321")

    assert result[0] == "Bob Smith"
    assert result[1]["email"] == "bob@example.com"


def test_search_by_phone_not_found():
    contacts = sample_contacts()

    result = search_by_phone(contacts, "000-0000000")

    assert result is None


def test_list_all_sorted():
    contacts = sample_contacts()

    result = list_all(contacts)
    names = [name for name, details in result]

    assert names == ["Alice Johnson", "Bob Smith", "Carol White"]


def test_get_cities():
    contacts = sample_contacts()

    result = get_cities(contacts)

    assert result == {"Nablus", "Ramallah"}


def test_get_recent():
    contacts = sample_contacts()

    result = get_recent(contacts, 2)

    assert result == [
        ("Bob Smith", "052-7654321"),
        ("Carol White", "053-1111111"),
    ]


def test_contacts_in_cities_union():
    contacts = sample_contacts()

    result = contacts_in_cities(contacts, "Nablus", "Ramallah")

    assert result["union"] == {
        "Alice Johnson",
        "Bob Smith",
        "Carol White",
    }


def test_contacts_in_cities_intersection():
    contacts = sample_contacts()

    result = contacts_in_cities(contacts, "Nablus", "Ramallah")

    assert result["intersection"] == set()
