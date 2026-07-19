import sqlite3

from data.database.connection import connect_database
from models.person import PersonCreate


def insert_person(person: PersonCreate) -> int:
    """
    PersonCreate 객체의 정보를 person 테이블에 저장한다.

    Args:
        person: 저장할 사람 정보

    Returns:
        새로 생성된 사람 ID
    """
    try:
        with connect_database() as connection:
            cursor = connection.execute(
                """
                INSERT INTO person (
                    name,
                    phone,
                    gender_id,
                    address
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    person.name,
                    person.phone,
                    person.gender_id,
                    person.address,
                ),
            )

            person_id = cursor.lastrowid

            if person_id is None:
                raise RuntimeError(
                    "사람 등록 후 ID를 가져오지 못했습니다."
                )

            return int(person_id)

    except sqlite3.IntegrityError as error:
        raise ValueError(
            f"사람 정보를 저장할 수 없습니다: {error}"
        ) from error

    except sqlite3.Error as error:
        raise RuntimeError(
            f"데이터베이스 처리 중 오류가 발생했습니다: {error}"
        ) from error