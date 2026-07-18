# normalizers/person.py
import re


def normalize_name(name: str) -> str:
    return name.strip()


def normalize_phone(phone: str) -> str:
    return re.sub(r"\D", "", phone)


def normalize_address(address: str) -> str:
    return address.strip()
