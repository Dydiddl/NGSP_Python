def select_main_menu() -> str:
    """프로그램의 주요 관리 대상을 선택받는다."""
    while True:
        print()
        print("========== Main Menu ==========")
        print("1. Person Management")
        print("2. Project Management")
        print("0. Exit")
        print("===============================")

        choice = input("Select: ").strip()

        if choice in ("0", "1", "2"):
            return choice

        print("Please select 0, 1, or 2.")