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





