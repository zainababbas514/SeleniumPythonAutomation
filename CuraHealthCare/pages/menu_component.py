from selenium.webdriver.common.by import By
from pages.history_page import HistoryPage
from pages.profile_page import ProfilePage

class MenuComponent:

    menu_toggle = (By.CSS_SELECTOR, "a#menu-toggle")
    login_option = (By.XPATH, "//*[@class='sidebar-nav']//li[3]")
    logout_option = (By.XPATH, "//a[normalize-space()='Logout']")
    history_option = (By.XPATH, "//a[normalize-space()='History']")
    profile_option = (By.XPATH, "//a[normalize-space()='Profile']")
    menu_options = (By.CSS_SELECTOR, "ul.sidebar-nav li:nth-child(n+3) a")

    def __init__(self, driver):
        self.driver = driver

    def open_menu(self):
        self.driver.find_element(*self.menu_toggle).click()

    def click_menu_login_option(self):
        self.driver.find_element(*self.login_option).click()

    def click_menu_logout_option(self):
        self.driver.find_element(*self.logout_option).click()

    def click_menu_history_option(self):
        self.driver.find_element(*self.history_option).click()
        return HistoryPage(self.driver)

    def click_profile_button(self):
        self.driver.find_element(*self.profile_option).click()
        return ProfilePage(self.driver)

    def is_login_option_visible(self):
        return self.driver.find_element(*self.login_option).is_displayed()

    def is_profile_option_visible(self):
        return self.driver.find_element(*self.profile_option).is_displayed()

    def is_history_option_displayed(self):
        return self.driver.find_element(*self.history_option).is_displayed()

    def is_logout_option_displayed(self):
        return self.driver.find_element(*self.logout_option).is_displayed()

    def get_visible_menu_options(self):
        options = self.driver.find_elements(*self.menu_options)
        return [option.text for option in options if option.is_displayed()]

    def verify_menu_options_for_guest(self):
        visible_options = self.get_visible_menu_options()
        assert 'Login' in visible_options
        assert 'Home' in visible_options
        for option in ['History', 'Profile', 'Logout']:
            assert option not in visible_options




