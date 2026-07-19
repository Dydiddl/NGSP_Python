from services.service_person import service_person_register_csv, service_person_register_manual

def select_person_menu() -> None:
    """사람 관리 기능을 선택받는다."""
    while True:
        print()
        print("========== Person Management ==========")
        print("1. Register Person")
        print("2. View People")
        print("0. Back")
        print("=======================================")

        choice = input("Select: ").strip()

        try:
            if choice == "0":
                return
            elif choice == "1":
                result = select_person_registration_method()
                print()
                print("사람 등록이 완료되었습니다.")
                print(f"Person ID: {result}")
            elif choice == "2":
                print("검색기능은 개발중입니다.")
            else:
                print("메뉴번호를 정확히 확인하세요.")

        except ValueError as error:
            print(f"처리 실패: {error}")
        except RuntimeError as error:
            print(f"프로그램 처리 중 문제가 발생했습니다: {error}")



def select_person_registration_method() -> str | None:
    """사람 등록 방법을 선택받는다."""
    while True:
        print()
        print("========== Person Registration ==========")
        print("1. Register People from CSV File")
        print("2. Register One Person Manually")
        print("0. Back")
        print("=========================================")

        choice = input("Select: ").strip()

        if choice == "0":
            return
        if choice == "1":
            service_person_register_csv()
        if choice == "2":
            service_person_register_manual()

        print("Please select 0, 1, or 2.")

def ask_register_another_person() -> bool:
    """사람을 한 명 더 수동 등록할 것인지 묻는다."""
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