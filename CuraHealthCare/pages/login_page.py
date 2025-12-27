from selenium.webdriver.common.by import By
from pages.appointment_page import AppointmentPage

class LoginPage:

    login_section = (By.XPATH, "//section[@id='login']")
    username_input = (By.XPATH, "//input[@id='txt-username']")
    password_input = (By.XPATH, "//input[@id='txt-password']")
    login_button = (By.XPATH, "//button[@id='btn-login']")
    login_error_message = (By.CSS_SELECTOR, ".lead.text-danger")

    def __init__(self, driver):
        self.driver = driver

    def check_login_form_visible(self):
        login_section_visible = self.driver.find_element(*self.login_section).is_displayed()
        username_input_visible = self.driver.find_element(*self.username_input).is_displayed()
        password_input_visible = self.driver.find_element(*self.password_input).is_displayed()
        login_button_visible = self.driver.find_element(*self.login_button).is_displayed()
        return login_section_visible and username_input_visible and password_input_visible and login_button_visible

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return AppointmentPage(self.driver)

    def verify_failed_login(self):
        error_message = self.driver.find_element(*self.login_error_message)
        assert error_message.is_displayed()
        assert "Login failed!" in error_message.text
        assert 'login' in self.driver.current_url



