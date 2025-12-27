from selenium.webdriver.common.by import By
from utils.base_class import BaseClass

class ProfilePage(BaseClass):

    profile_page_heading = (By.CSS_SELECTOR, "#profile h2")
    logout_button = (By.XPATH, "//p//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def verify_profile_page_loaded(self):
        self.wait_for_url(self.profile_page_heading)
        assert "profile" in self.driver.current_url, "URL does not contain 'profile'"

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()



