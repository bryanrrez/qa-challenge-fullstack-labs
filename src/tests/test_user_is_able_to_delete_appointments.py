
from src.pages.home import HomePage
from src.support.commands import Commands


def test_user_is_able_to_delete_appointments(driver, appointments):
    APPOINTMENT = appointments['valid_appointment']

    commands = Commands(driver)
    commands.add_appointment(APPOINTMENT)

    home_page = HomePage(driver)

    home_page.click_delete_button()

    assert home_page.get_dynamic_title() == 'THERE ARE NO APPOINTMENTS'