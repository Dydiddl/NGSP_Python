# 파이썬 기본 SQLite 라이브러리
# 데이터베이스 연결, SQL 실행, 결과 가져오기, 트랜잭션 처리(?)
import sqlite3

# 다른 파일에 만들어 둔 클래스를 가져온다.
from models.person import PersonCreate
from config import DATABASE_PATH


def connect_database() -> sqlite3.Connection:
    """
    SQLite database connection string to connect to
    :return:
    """
    # parents=True -> 폴더가 없으면 만들어라,
    # exist_ok=True -> 폴더가 있으면 넘어가라
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    # DATABASE_PATH 위치의 SQLite 데이터베이스에 연결하고,
    # SQL을 실행할 수 있는 Connection 객체를 생성한다.
    connection = sqlite3.connect(DATABASE_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection

def create_tables() -> None:
    """
    SQLite database connection string to create tables
    :return:
    """
    with connect_database() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS gender(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO gender (id, name)
            VALUES 
                (1, 'Male'),
                (2, 'Female') 
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                gender_id INTEGER NOT NULL REFERENCES gender(id),
                address TEXT
            )
            """
        )

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
