import re

from config.validation import (
    PERSON_ADDRESS_MAX_LENGTH,
    PERSON_NAME_MAX_LENGTH,
    PERSON_NAME_MIN_LENGTH,
    PERSON_PHONE_LENGTH,
    PERSON_PHONE_PREFIX,
    PERSON_VALID_GENDER_IDS,
)
from models.person import PersonCreate


def validate_name(name: str) -> str:
    normalized_name = name.strip()

    if not normalized_name:
        raise ValueError("이름을 입력해야 합니다.")

    if len(normalized_name) < PERSON_NAME_MIN_LENGTH:
        raise ValueError(
            f"이름은 최소 {PERSON_NAME_MIN_LENGTH}글자 이상이어야 합니다."
        )

    if len(normalized_name) > PERSON_NAME_MAX_LENGTH:
        raise ValueError(
            f"이름은 최대 {PERSON_NAME_MAX_LENGTH}글자까지 입력할 수 있습니다."
        )

    return normalized_name


def normalize_phone(phone: str) -> str:
    normalized_phone = re.sub(r"\D", "", phone)

    if len(normalized_phone) != PERSON_PHONE_LENGTH:
        raise ValueError(
            f"전화번호는 숫자 {PERSON_PHONE_LENGTH}자리여야 합니다."
        )

    if not normalized_phone.startswith(PERSON_PHONE_PREFIX):
        raise ValueError(
            f"전화번호는 {PERSON_PHONE_PREFIX}으로 시작해야 합니다."
        )

    return normalized_phone


def validate_gender_id(gender_id: int) -> int:
    if gender_id not in PERSON_VALID_GENDER_IDS:
        raise ValueError(
            f"성별 ID는 {PERSON_VALID_GENDER_IDS} 중 하나여야 합니다."
        )

    return gender_id


def validate_address(address: str) -> str:
    normalized_address = address.strip()

    if not normalized_address:
        raise ValueError("주소를 입력해야 합니다.")

    if len(normalized_address) > PERSON_ADDRESS_MAX_LENGTH:
        raise ValueError(
            f"주소는 최대 {PERSON_ADDRESS_MAX_LENGTH}글자까지 입력할 수 있습니다."
        )

    return normalized_address


def validate_person(person: PersonCreate) -> PersonCreate:
    return PersonCreate(
        name=validate_name(person.name),
        phone=normalize_phone(person.phone),
        gender_id=validate_gender_id(person.gender_id),
        address=validate_address(person.address),
    )