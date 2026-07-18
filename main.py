from ui.input_person import input_person
from importers.importer_person_csv import import_persons_from_csv
from repositories.repository_person import create_tables, insert_person


def select_registration_method() -> str:
    """사람 등록 방법을 선택받는다."""

    while True:
        print()
        print("========== Person Registration ==========")
        print("1. Register people from CSV file")
        print("2. Register one person manually")
        print("0. Exit")
        print("=========================================")

        choice = input("Select: ").strip()

        if choice in ("0", "1", "2"):
            return choice

        print("Please select 0, 1, or 2.")


def ask_continue() -> bool:
    """직접 입력을 계속할 것인지 묻는다."""

    while True:
        print()
        choice = input(
            "Would you like to register another person? (y/n): "
        ).strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter y or n.")


def register_person_manually() -> None:
    """사람을 한 명씩 직접 입력하여 등록한다."""

    while True:
        person = input_person()

        try:
            person_id = insert_person(person)

            print()
            print("The person has been registered successfully.")
            print(f"Person ID: {person_id}")
            print(f"Name: {person.name}")

        except Exception as error:
            print()
            print("Person registration failed.")
            print(f"Reason: {error}")

        if not ask_continue():
            print("Manual registration has ended.")
            return


def register_persons_from_csv() -> None:
    """설정된 CSV 파일에서 사람들을 일괄 등록한다."""

    print()
    print("CSV registration has started.")

    try:
        result = import_persons_from_csv()

    except FileNotFoundError as error:
        print()
        print("CSV file could not be found.")
        print(error)
        return

    except ValueError as error:
        print()
        print("The CSV file structure is incorrect.")
        print(error)
        return

    except Exception as error:
        print()
        print("An unexpected error occurred.")
        print(error)
        return

    print()
    print("========== CSV Registration Result ==========")
    print(f"Successful: {result.success_count}")
    print(f"Failed: {len(result.errors)}")
    print("=============================================")

    if result.errors:
        print()
        print("Failed rows")

        for error in result.errors:
            print(
                f"- Row {error.row_number}: "
                f"{error.name or '(No name)'} / "
                f"{error.reason}"
            )


def main() -> None:
    """프로그램 실행 함수."""

    create_tables()

    choice = select_registration_method()

    if choice == "1":
        register_persons_from_csv()

    elif choice == "2":
        register_person_manually()

    else:
        print("The program has ended.")


if __name__ == "__main__":
    main()