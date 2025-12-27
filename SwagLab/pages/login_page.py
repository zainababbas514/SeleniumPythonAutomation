from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

class LoginPage:

    username_input = (By.XPATH, "//input[@name='user-name']")
    password_input = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//input[@name='login-button']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
        return InventoryPage(self.driver)


