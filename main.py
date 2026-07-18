from ui.menu_person import select_registration_method, register_person_manually
from importers.importer_person_csv import import_persons_from_csv
from repositories.repository_person import create_person_tables, insert_person



def main() -> None:
    """프로그램 실행 함수."""
    create_person_tables()

    choice = select_registration_method()

    if choice == "1":
        import_persons_from_csv()
    elif choice == "2":
        register_person_manually()
    else:
        print("The program has ended.")
if __name__ == "__main__":
    main()