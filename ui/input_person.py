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
