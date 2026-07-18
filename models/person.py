import dataclasses

@dataclasses.dataclass
class Person:
    id: int
    name: str
    phone: str
    gender_id: int
    address: str | None = None

@dataclasses.dataclass
class PersonCreate:
    name: str
    phone: str
    gender_id: int
    address: str | None = None
