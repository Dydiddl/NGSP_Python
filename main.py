from ui.menus.menu_main import select_main_menu
from data.database.initialize import initialize_database

def main() -> None:
    """프로그램을 초기화하고 메인 메뉴를 실행한다."""
    initialize_database()
    select_main_menu()

if __name__ == "__main__":
    main()