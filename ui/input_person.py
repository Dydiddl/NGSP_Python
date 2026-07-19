from models.person import PersonCreate
from normalizers.normalizer_person import (
    normalize_name,
    normalize_phone,
    convert_gender_id,
    normalize_address
)
from validators.validator_person import (
    validate_name,
    validate_phone,
    validate_gender_id,
    validate_address
)


def input_person() -> PersonCreate:
    name = input_name()
    phone = input_phone()
    gender_id = input_gender_id()
    address = input_address()
    return PersonCreate(
        name=name,
        phone=phone,
        gender_id=gender_id,
        address=address
    )

def input_name() -> str:
    while True:
        raw_name = input("Please enter person's name: ")
        try:
            name = normalize_name(raw_name)
            validate_name(name)
            return name
        except ValueError as error:
            print(error)

def input_phone() -> str:
     while True:
            raw_phone = input("Please enter person's phone number: ")
            try:
                phone = normalize_phone((raw_phone))
                validate_phone(phone)
                return phone
            except ValueError as error:
                print(error)

def input_gender_id() -> int:
    while True:
        print("1. Male")
        print("2. Female")
        raw_gender_id = input("Please select person's gender id: ")
        try:
            gender_id = convert_gender_id((raw_gender_id))
            validate_gender_id(gender_id)
            return gender_id
        except ValueError as error:
            print(error)

def input_address() -> str:
    while True:
        raw_address = input("Please enter your address: ")
        try:
            address = normalize_address((raw_address))
            validate_address(address)
            return address
        except ValueError as error:
            print(error)