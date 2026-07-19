
def ui_insert_person_manually():

    print("========== Person Manual ==========")

    name = input_name()

    phone = input_phone()

    gender = input_gender()

    address = input_address()

    insert_person(
        name,
        phone,
        gender,
        address,
    )