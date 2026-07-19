# 파이썬 기본 SQLite 라이브러리
# 데이터베이스 연결, SQL 실행, 결과 가져오기, 트랜잭션 처리(?)
import sqlite3
import data.database.connection as connect_database
# 다른 파일에 만들어 둔 클래스를 가져온다.
from models.person import PersonCreate


def insert_person(person: PersonCreate) -> int:
    """
    Person 객체의 정보를 person 테이블에 저장한다.
    :param person: 저장할 사람 정보
    :return: 새로 생성된 person 테이블의 ID
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
                raise RuntimeError("사람 등록에 실패했습니다.")
            return int(person_id)

    except sqlite3.IntegrityError as error:
        raise ValueError(
            f"사람 정보를 저장할 수 없습니다: {error}"
        ) from error
