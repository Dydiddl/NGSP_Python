import csv
import re
from dataclasses import dataclass
from pathlib import Path

from config import PERSON_INPUT_CSV_PATH
from models.person import PersonCreate
from repositories.repository_person import insert_person


@dataclass
class CsvImportError:
    """CSV 등록 실패 정보를 저장한다."""

    row_number: int
    name: str
    reason: str


@dataclass
class CsvImportResult:
    """CSV 전체 등록 결과를 저장한다."""

    success_count: int
    errors: list[CsvImportError]


def clean_value(value: str | None) -> str:
    """CSV 값의 앞뒤 공백을 제거한다."""

    if value is None:
        return ""

    return value.strip()


def validate_csv_headers(fieldnames: list[str] | None) -> None:
    """CSV에 필요한 열이 모두 있는지 검사한다."""

    required_headers = {
        "name",
        "phone",
        "gender_id",
        "address",
    }

    actual_headers = set(fieldnames or [])
    missing_headers = required_headers - actual_headers

    if missing_headers:
        missing_text = ", ".join(sorted(missing_headers))

        raise ValueError(
            f"CSV에 필요한 열이 없습니다: {missing_text}"
        )


def validate_name(name: str) -> None:
    """이름을 검사한다."""

    if not name:
        raise ValueError("이름이 비어 있습니다.")

    if len(name) < 2:
        raise ValueError("이름은 최소 2글자 이상이어야 합니다.")


def validate_phone(phone: str) -> None:
    """전화번호 형식을 검사한다."""

    if not phone:
        raise ValueError("전화번호가 비어 있습니다.")

    phone_pattern = re.compile(r"^010-\d{4}-\d{4}$")

    if not phone_pattern.fullmatch(phone):
        raise ValueError(
            "전화번호는 010-0000-0000 형식이어야 합니다."
        )


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


def validate_address(address: str) -> None:
    """주소를 검사한다."""

    if not address:
        raise ValueError("주소가 비어 있습니다.")


def create_person_from_row(row: dict[str, str]) -> PersonCreate:
    """CSV 한 행을 PersonCreate 객체로 변환한다."""

    name = clean_value(row.get("name"))
    phone = clean_value(row.get("phone"))
    gender_value = clean_value(row.get("gender_id"))
    address = clean_value(row.get("address"))

    validate_name(name)
    validate_phone(phone)
    gender_id = convert_gender_id(gender_value)
    validate_address(address)

    return PersonCreate(
        name=name,
        phone=phone,
        gender_id=gender_id,
        address=address,
    )


def open_csv_file(csv_path: Path):
    """
    CSV 파일을 연다.

    현재 person_input.csv가 CP949로 저장되어 있으므로
    우선 CP949로 연다.
    """

    return csv_path.open(
        mode="r",
        encoding="cp949",
        newline="",
    )


def import_persons_from_csv(
    csv_path: Path = PERSON_INPUT_CSV_PATH,
) -> CsvImportResult:
    """CSV 파일의 사람들을 데이터베이스에 일괄 등록한다."""

    if not csv_path.exists():
        raise FileNotFoundError(
            f"CSV 파일을 찾을 수 없습니다: {csv_path}"
        )

    success_count = 0
    errors: list[CsvImportError] = []

    with open_csv_file(csv_path) as csv_file:
        reader = csv.DictReader(csv_file)

        validate_csv_headers(reader.fieldnames)

        # 1행은 헤더이므로 실제 데이터는 2행부터 시작한다.
        for row_number, row in enumerate(reader, start=2):
            name = clean_value(row.get("name"))

            try:
                person = create_person_from_row(row)
                person_id = insert_person(person)

                success_count += 1

                print(
                    f"[등록 성공] {row_number}행 "
                    f"{person.name} / ID: {person_id}"
                )

            except Exception as error:
                errors.append(
                    CsvImportError(
                        row_number=row_number,
                        name=name,
                        reason=str(error),
                    )
                )

                print(
                    f"[등록 실패] {row_number}행 "
                    f"{name or '(이름 없음)'} / {error}"
                )

    return CsvImportResult(
        success_count=success_count,
        errors=errors,
    )