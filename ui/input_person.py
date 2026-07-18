from models.person import PersonCreate
from validators.validator_person import (
normalize_phone,
validate_name,
validate_gender_id,
validate_address,
)


def input_name() -> str:
    while True:
        try:
            return validate_name(input("Please enter your name: "))
        except ValueError as error:
            print(error)

def input_phone() -> str:
    while True:
        try:
            return normalize_phone(input("Please enter your phone number: "))
        except ValueError as error:
            print(error)

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
