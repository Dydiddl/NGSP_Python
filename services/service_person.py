from models.person import PersonCreate
from ui.input_person import input_person

def insert_person(
    name,
    phone,
    gender,
    address,
):

    person = PersonCreate(
        name=name,
        phone=phone,
        gender_id=gender,
        address=address,
    )

 

def service_person_register_csv():
    return

def service_person_register_manual():
    """사용자로부터 한 사람의 정보를 입력받아 데이터베이스에 등록한다."""
    person_create = input_person()
    person_id = insert_person(person_create)
    return