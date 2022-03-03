from src.pages.home import HomePage


def test_user_is_able_to_add_appointments(driver, appointments):
    APPOINTMENT = appointments['valid_appointment']

    home_page = HomePage(driver)
    home_page.type_pet_name(APPOINTMENT['pet_name'])
    home_page.type_owner_name(APPOINTMENT['owner_name'])
    home_page.type_date(APPOINTMENT['date'])
    home_page.type_time(APPOINTMENT['time'])
    home_page.type_symptoms(APPOINTMENT['symptoms'])
    home_page.click_add_appointment()

    assert home_page.get_dynamic_title() == 'MANAGE YOUR APPOINTMENTS'