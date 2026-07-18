import dataclasses

@dataclasses.dataclass
class Person:
    id: int
    name: str
    phone: str
    gender_id: int
    address: str

@dataclasses.dataclass
class PersonCreate:
    name: str
    phone: str
    gender_id: int
    address: str
