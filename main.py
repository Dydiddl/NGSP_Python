from ui.input_person import select_registration_method, register_persons_from_csv, register_person_manually
from importers.importer_person_csv import import_persons_from_csv
from repositories.repository_person import create_tables, insert_person



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