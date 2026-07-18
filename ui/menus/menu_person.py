def select_person_menu() -> str:
    """사람 관리 기능을 선택받는다."""
    while True:
        print()
        print("========== Person Management ==========")
        print("1. Register Person")
        print("2. View People")
        print("0. Back")
        print("=======================================")

        choice = input("Select: ").strip()

        if choice in ("0", "1", "2"):
            return choice

        print("Please select 0, 1, or 2.")


def select_person_registration_method() -> str:
    """사람 등록 방법을 선택받는다."""
    while True:
        print()
        print("========== Person Registration ==========")
        print("1. Register People from CSV File")
        print("2. Register One Person Manually")
        print("0. Back")
        print("=========================================")

        choice = input("Select: ").strip()

        if choice in ("0", "1", "2"):
            return choice

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