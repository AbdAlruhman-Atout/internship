import pytest

from contacts import (
    add_contact,
    remove_contact,
    update_contact,
    search_by_name,
    search_by_phone,
    load_contacts,
    save_contacts,
    get_summary,
)


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
    }


def test_load_missing_file(tmp_path):
    filepath = tmp_path / "missing.json"

    result = load_contacts(filepath)

    assert result == {}


def test_save_and_load_roundtrip(tmp_path):
    filepath = tmp_path / "contacts.json"
    contacts = sample_contacts()

    save_contacts(contacts, filepath)
    result = load_contacts(filepath)

    assert result == contacts


def test_add_contact_keyword_only():
    contacts = sample_contacts()

    add_contact(
        contacts,
        "Carol White",
        phone="053-1111111",
        email="carol@example.com",
        city="Hebron",
    )

    assert "Carol White" in contacts


def test_add_duplicate_raises():
    contacts = sample_contacts()

    with pytest.raises(ValueError):
        add_contact(
            contacts,
            "Alice Johnson",
            phone="059-9999999",
            email="alice2@example.com",
            city="Jenin",
        )


def test_remove_contact():
    contacts = sample_contacts()

    remove_contact(contacts, "Bob Smith")

    assert "Bob Smith" not in contacts


def test_update_partial_fields():
    contacts = sample_contacts()

    update_contact(contacts, "Alice Johnson", city="Hebron")

    assert contacts["Alice Johnson"]["city"] == "Hebron"
    assert contacts["Alice Johnson"]["phone"] == "059-1234567"
    assert contacts["Alice Johnson"]["email"] == "alice@example.com"


def test_search_by_name_partial():
    contacts = sample_contacts()

    result = search_by_name(contacts, "alice")

    assert len(result) == 1
    assert result[0][0] == "Alice Johnson"


def test_search_by_phone():
    contacts = sample_contacts()

    result = search_by_phone(contacts, "052-7654321")

    assert result[0] == "Bob Smith"


def test_get_summary_tuple():
    contacts = sample_contacts()

    total, cities, avg_per_city = get_summary(contacts)

    assert total == 2
    assert cities == {"Nablus", "Ramallah"}
    assert avg_per_city == 1.0


def test_get_summary_avg():
    contacts = sample_contacts()

    add_contact(
        contacts,
        "Carol White",
        phone="053-1111111",
        email="carol@example.com",
        city="Nablus",
    )

    total, cities, avg_per_city = get_summary(contacts)

    assert total == 3
    assert cities == {"Nablus", "Ramallah"}
    assert avg_per_city == 1.5
