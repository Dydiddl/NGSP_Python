from ui.menus.menu_person import select_person_menu


def select_main_menu() -> str | None:
    """프로그램의 주요 관리 대상을 선택받는다."""
    while True:
        print("              Namgang Landscape System             ")
        print("==================== Main Menu ====================")
        print("1. Person Management")
        print("2. Project Management")
        print("0. Exit")
        print("===================================================")

        choice = input("Select: ").strip()

        if choice == 0:
            print("프로그램을 종료합니다.")
            break
        if choice == 1:
            select_person_menu()
        if choice == 2:
            print("2. Project Management는 개발중입니다.")


        print("Please select 0, 1, or 2.")