# normalizers/person.py
import re


def normalize_name(value: str | None) -> str:
    """CSV 값의 앞뒤 공백을 제거한다."""
    return value.strip()

def normalize_phone(phone: str) -> str:
    """
    전화번호에서 숫자가 아닌 문자를 제거한다.
    :param phone:
    :return:
    """
    return re.sub(r"\D", "", phone)


def normalize_address(address: str) -> str:
    """주소의 앞뒤 공백을 제거한다."""
    return address.strip()

def convert_gender_id(value: str) -> int:
    """gender_id를 정수로 변환하고 검사한다."""

    if not value:
        raise ValueError("성별 ID가 비어 있습니다.")

    try:
        gender_id = int(value)

    except ValueError as error:
        raise ValueError(
            "성별 ID는 숫자여야 합니다."
        ) from error

    if gender_id not in (1, 2):
        raise ValueError("성별 ID는 1 또는 2여야 합니다.")

    return gender_id