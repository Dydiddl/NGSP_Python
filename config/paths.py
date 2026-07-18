from pathlib import Path

# 프로젝트 경로
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 폴더 경로
RESOURCE_DIR = PROJECT_ROOT / "data"
DATABASE_DIR = PROJECT_ROOT / "database"

INPUT_DIR = RESOURCE_DIR / "input"

# 파일 경로
DATABASE_PATH = DATABASE_DIR / "database.db"
PERSON_INPUT_CSV_PATH = INPUT_DIR / "person_input.csv"

# 입력 규칙
MIN_NAME_LENGTH = 2
PHONE_PREFIX = "010"
DEFAULT_NATIONALITY = "KR"

# 표시 설정
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"