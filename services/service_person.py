from importers.importer_person_csv import import_persons_from_csv
from models.person import PersonCreate
from ui.input_person import input_person


def service_person_register_csv():
    """
    CSV 파일에 있는 사람들을 데이터베이스에 등록한다.

    :return:
        성공 개수와 실패 개수
    """
    return import_persons_from_csv()

def service_person_register_manual(person: PersonCreate) -> int:
    """
    사람 정보를 수동으로 입력받아 데이터베이스에 등록한다.

    :return:
        새롭게 등록된 사람의 ID
    """
    return insert_person(person)