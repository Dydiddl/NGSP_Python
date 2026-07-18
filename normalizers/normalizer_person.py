# normalizers/person.py
import re


def normalize_name(value: str ) -> str:
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