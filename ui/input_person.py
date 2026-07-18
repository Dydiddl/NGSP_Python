from models.person import PersonCreate
from validators.validator_person import (
normalize_phone,
validate_name,
validate_gender_id,
validate_address,
)

def select_registration_method() -> str:
    """사람 등록 방법을 선택받는다."""
    while True:
        print()
        print("========== Person Registration ==========")
        print("1. Register people from CSV file")
        print("2. Register one person manually")
        print("0. Exit")
        print("=========================================")
        choice = input("Select: ").strip()
        if choice in ("0", "1", "2"):
            return choice
        print("Please select 0, 1, or 2.")

def ask_continue() -> bool:
    """직접 입력을 계속할 것인지 묻는다."""
    while True:
        print()
        choice = input(
            "Would you like to register another person? (y/n): "
        ).strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter y or n.")

def register_person_manually() -> None:
    """사람을 한 명씩 직접 입력하여 등록한다."""
    while True:
        person = input_person()
        try:
            person_id = insert_person(person)
            print()
            print("The person has been registered successfully.")
            print(f"Person ID: {person_id}")
            print(f"Name: {person.name}")
        except Exception as error:
            print()
            print("Person registration failed.")
            print(f"Reason: {error}")
        if not ask_continue():
            print("Manual registration has ended.")
            return




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
