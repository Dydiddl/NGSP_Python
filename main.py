from repositories.repository_person import create_person_tables
from services.service_person import register_persons_from_csv
from ui.input_person import register_person_manually
from ui.menus.menu_main import select_main_menu
from ui.menus.menu_person import (
    select_person_menu,
    select_person_registration_method,
)


def run_person_registration_menu() -> None:
    """사람 등록 방법 메뉴를 실행한다."""
    while True:
        choice = select_person_registration_method()

        if choice == "0":
            return

        if choice == "1":
            register_persons_from_csv()
            continue

        if choice == "2":
            register_person_manually()


def run_person_menu() -> None:
    """사람 관리 메뉴를 실행한다."""
    while True:
        choice = select_person_menu()

        if choice == "0":
            return

        if choice == "1":
            run_person_registration_menu()
            continue

        if choice == "2":
            print()
            print("View people is not implemented yet.")


def main() -> None:
    """프로그램을 초기화하고 메인 메뉴를 실행한다."""
    create_tables()

    while True:
        choice = select_main_menu()

        if choice == "0":
            print()
            print("The program has ended.")
            return

        if choice == "1":
            run_person_menu()
            continue

        if choice == "2":
            print()
            print("Project management is not implemented yet.")


if __name__ == "__main__":
    main()