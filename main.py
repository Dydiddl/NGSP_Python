from formatters.formatter_person import format_phone
from ui.input_person import input_person

def main() -> None:
    """프로그램 실행 함수."""
    person = input_person()

    print("\n입력 결과")
    print(f"name: {person.name}")
    print(f"phone: {format_phone(person.phone)}")
    print(f"gender_id: {person.gender_id}")
    print(f"address: {person.address}")

if __name__ == "__main__":
    main()