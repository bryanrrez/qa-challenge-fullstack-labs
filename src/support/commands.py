

from src.pages.home import HomePage

class Commands:

    def __init__(self, driver):
        self.driver = driver

    def add_appointment(self, appointment):
        home_page = HomePage(self.driver)
        home_page.type_pet_name(appointment['pet_name'])
        home_page.type_owner_name(appointment['owner_name'])
        home_page.type_date(appointment['date'])
        home_page.type_time(appointment['time'])
        home_page.type_symptoms(appointment['symptoms'])
        home_page.click_add_appointment()