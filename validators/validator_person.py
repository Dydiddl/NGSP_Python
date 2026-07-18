from config.validation import (
    PERSON_ADDRESS_MAX_LENGTH,
    PERSON_NAME_MAX_LENGTH,
    PERSON_NAME_MIN_LENGTH,
    PERSON_PHONE_LENGTH,
    PERSON_PHONE_PREFIX,
    PERSON_VALID_GENDER_IDS,
)
from models.person import PersonCreate

def validate_name(name: str) -> None:
    if not name:
        raise ValueError(f"The name is empty.")
    if len(name) > PERSON_NAME_MIN_LENGTH:
        raise ValueError(f"The name must be at least {PERSON_NAME_MIN_LENGTH} characters long.")
    if len(name) > PERSON_NAME_MAX_LENGTH:
        raise ValueError(f"The name must be at most {PERSON_NAME_MAX_LENGTH} characters long.")

def validate_phone(phone: str) -> None:
    if not phone:
        raise ValueError(f"The phone number is empty.")
    if not phone.isdigit():
        raise ValueError(f"The phone numbers must be numbers only.")
    if len(phone) != PERSON_PHONE_LENGTH:
        raise ValueError(f"The phone number must be {PERSON_PHONE_LENGTH}digits only.")
    if not phone.startswith(PERSON_PHONE_PREFIX):
        raise ValueError(f"The phone number must start with {PERSON_PHONE_PREFIX}.")


def validate_gender_id(gender_id: int) -> None:
    if gender_id not in PERSON_VALID_GENDER_IDS:
        raise ValueError(f"성별 ID는 {PERSON_VALID_GENDER_IDS} 중 하나여야 합니다.")

def validate_address(address: str) -> None:
    if not address:
        raise ValueError(f"The address is empty.")
    if len(address) > PERSON_ADDRESS_MAX_LENGTH:
        raise ValueError(f"The address must be at most {PERSON_ADDRESS_MAX_LENGTH} characters long.")

def validate_person(person: PersonCreate) -> None:
    validate_name(person.name)
    validate_phone(person.phone)
    validate_gender_id(person.gender_id)
    validate_address(person.address)