from importers.importer_person_csv import import_persons_from_csv

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