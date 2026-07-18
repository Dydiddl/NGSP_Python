from config import validation
from models.person import PersonCreate


def input_name() -> str:
    while True:
        name = input("Please enter your name: ").strip()
        if validation.is_valid_name(name):
            return name
        print("The name must be at least two characters long")

def input_phone() -> str:
    while True:
        phone = input("phone : ").strip()
        if validation.is_valid_phone(phone):
            return phone
        print("The mobile phone number format is incorrect")

def input_gender() -> int:
    while True:
        print("1. Male")
        print("2. Female")
        choice = input("Select Gender(Number): ").strip()
        if choice in ("1", "2"):
            return int(choice)
        print("The gender must be between 1 and 2")

def input_address() -> str | None:
    address = input("Please enter your address: ").strip()
    return address or None

def input_person() -> PersonCreate:
    return PersonCreate(
        name=input_name(),
        phone=input_phone(),
        gender_id=input_gender(),
        address=input_address(),
    )
