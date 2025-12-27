from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class HomePage:

    book_appointment_button = (By.CSS_SELECTOR, "a#btn-make-appointment")

    def __init__(self, driver):
        self.driver = driver

    def click_book_appointment_button(self):
        self.driver.find_element(*self.book_appointment_button).click()
        return LoginPage(self.driver)









