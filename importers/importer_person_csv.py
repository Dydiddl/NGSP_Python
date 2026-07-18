import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, TextIO

from config.paths import PERSON_INPUT_CSV_PATH
from config.validation import PERSON_CSV_REQUIRED_COLUMNS, PERSON_CSV_ENCODING
from models.person import PersonCreate
from normalizers.normalizer_person import (
    normalize_name,
    normalize_phone,
    normalize_address
)
from repositories.repository_person import insert_person
from validators.validator_person import validate_person


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


def get_csv_value(
        row: dict[str, str | None],
        column_name: str,
) -> str:
    """
    csv 행에서 값을 가져온다.

    csv 셀 값이 없으면 빈 문자열을 반환한다.
    공백 제거와 형식 통이릉ㄴ person normalizer가 담당한다.
    :param row: csv에서 읽은 한 행
    :param column_name: 가져올 열 이름
    :return: 열의 값, 값이 없으면 빈 문자열
    """
    return row.get(column_name) or ""


def validate_csv_headers(
        fieldnames: Sequence[str] | None,
) -> None:
    """
    csv에 피룡한 열이 모두 있는지 검사한다.
    :param fieldnames:
    :return:
    """
    required_headers = set(PERSON_CSV_REQUIRED_COLUMNS)
    actual_headers = set(fieldnames or [])

    missing_headers = required_headers - actual_headers

    if missing_headers:
        missing_text = ", ".join(sorted(missing_headers))

        raise ValueError(
            f"csv에 필요한 열이 없습니다: {missing_text}"
        )


def convert_gender_id(value: str) -> int:
    """
    CSV에서 읽은 gender_id 문자열을 정수로 변환한다.
    허용되는 성별 ID인지 확인하는 작업은 validator_person.validate_gender_id()가 담당한다.
    """
    if not value:
        raise ValueError("성별 ID가 비어 있습니다.")
    try:
        return int(value)
    except ValueError as error:
        raise ValueError(
            "성별 ID는 숫자여야 합니다."
        ) from error


def create_person_from_row(
        row: dict[str, str | None],
) -> PersonCreate:
    """
    CSV 한 행을 PersonCreate 객체로 변환한다.
    """
    name = normalize_name(
        get_csv_value(row, "name")
    )
    phone = normalize_phone(
        get_csv_value(row, "phone")
    )
    gender_id = convert_gender_id(
        get_csv_value(row, "gender_id").strip()
    )
    address = normalize_address(
        get_csv_value(row, "address")
    )
    person = PersonCreate(
        name=name,
        phone=phone,
        gender_id=gender_id,
        address=address,
    )
    validate_person(person)
    return person


def open_csv_file(csv_path: Path) -> TextIO:
    """
    CSV 파일을 연다.

    현재 person_input.csv가 CP949로 저장되어 있으므로
    우선 CP949로 연다.
    """

    return csv_path.open(
        mode="r",
        encoding=PERSON_CSV_ENCODING,
        newline="",
    )


def import_persons_from_csv(
        csv_path: Path = PERSON_INPUT_CSV_PATH,
) -> CsvImportResult:
    """
    CSV 파일의 사람들을 데이터베이스에 일괄 등록한다.
    """
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
            name = normalize_name(
                get_csv_value(row, "name")
            )
            try:
                person = create_person_from_row(row)
                insert_person(person)
                success_count += 1
            except ValueError as error:
                errors.append(
                    CsvImportError(
                        row_number=row_number,
                        name=name,
                        reason=str(error),
                    )
                )
    return CsvImportResult(
        success_count=success_count,
        errors=errors,
    )