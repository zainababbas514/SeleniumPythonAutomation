from selenium.webdriver.common.by import By
from pages.checkout_page_two import CheckoutPageTwo

class CheckoutPageOne:

    first_name_input = (By.CSS_SELECTOR, "input#first-name")
    last_name_input = (By.CSS_SELECTOR, "input#last-name")
    postal_code_input = (By.CSS_SELECTOR, "input#postal-code")
    continue_button = (By.CSS_SELECTOR, "input#continue")

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name_input).send_keys(name)

    def enter_last_name(self, name):
        self.driver.find_element(*self.last_name_input).send_keys(name)

    def enter_postal_code(self, code):
        self.driver.find_element(*self.postal_code_input).send_keys(code)

    def fill_checkout_form(self, firstname, lastname, postal_code):
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_postal_code(postal_code)

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()
        return CheckoutPageTwo(self.driver)

