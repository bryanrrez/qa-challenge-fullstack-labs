
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def pet_name_input(cls):
        return (By.CSS_SELECTOR, 'input[data-testid="pet"]')

    @classmethod
    def owner_name_input(cls):
        return (By.CSS_SELECTOR, 'input[data-testid="owner"]')

    @classmethod
    def date_input(cls):
        return (By.CSS_SELECTOR, 'input[data-testid="date"]')

    @classmethod
    def time_input(cls):
        return (By.CSS_SELECTOR, 'input[data-testid="time"]')

    @classmethod
    def symptoms_textarea(cls):
        return (By.CSS_SELECTOR, 'textarea[data-testid="symptoms"]')

    @classmethod
    def add_appointment_button(cls):
        return (By.CSS_SELECTOR, 'button[data-testid="btn-submit"]')

    @classmethod
    def dynamic_title_h2(cls):
        return (By.CSS_SELECTOR, 'h2[data-testid="dynamic-title"]')

    @classmethod
    def delete_button(cls):
        return (By.CSS_SELECTOR, 'button[data-testid="btn-delete"]')

    def type_pet_name(self, pet_name):
        input = self.driver.find_element(*self.pet_name_input())
        input.clear()
        input.send_keys(pet_name)

    def type_owner_name(self, owner_name):
        input = self.driver.find_element(*self.owner_name_input())
        input.clear()
        input.send_keys(owner_name)

    def type_date(self, date):
        input = self.driver.find_element(*self.date_input())
        input.clear()
        input.send_keys(date.replace('/', ''))

    def type_time(self, time):
        input = self.driver.find_element(*self.time_input())
        input.clear()
        input.send_keys(time.replace(':', '').replace(' ', ''))

    def type_symptoms(self, symptoms):
        textarea = self.driver.find_element(*self.symptoms_textarea())
        textarea.clear()
        textarea.send_keys(symptoms)

    def click_add_appointment(self):
        button = self.driver.find_element(*self.add_appointment_button())
        button.click()

    def get_dynamic_title(self):
        return self.driver.find_element(*self.dynamic_title_h2()).text

    def click_delete_button(self):
        button = self.driver.find_element(*self.delete_button())
        button.click()