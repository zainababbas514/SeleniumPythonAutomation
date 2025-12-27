import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from utils.base_class import BaseClass
from pages.menu_component import MenuComponent

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("init_browser")
class TestLogout(BaseClass):
    logger = BaseClass.get_logger()

    # Login Credentials
    creds = BaseClass.get_data_from_json("credentials.json")
    username = creds['login_credentials']['username']
    password = creds['login_credentials']['password']

    def test_profile_page_logout(self):
        # Initialize page objects
        home_page = HomePage(self.driver)
        menu_component = MenuComponent(self.driver)

        self.logger.info("Starting TC-009: Verify the user can logout from the profile page.")

        # Clicking the Make Appointment button to display the login form
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info(f"The user is logging in with username {self.username} and password {self.password}")
        appointment_page = login_page.login(self.username, self.password)
        appointment_page.verify_appointment_form_visible()
        self.logger.info("The user is logged in successfully")

        self.logger.info("The user is opening the menu")
        menu_component.open_menu()

        self.logger.info("The user is clicking the profile page option from the menu")
        profile_page = menu_component.click_profile_button()

        self.logger.info("Clicking the logout button on the profile page")
        profile_page.click_logout_button()

        self.logger.info("Waiting for the home page to complete loading")
        self.wait_for_url("https://katalon-demo-cura.herokuapp.com/")

        # Clicking the Make Appointment button to verify the user successfully logged out
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info("Verifying login form is displayed with username, password field and the login button")
        assert login_page.check_login_form_visible(), "Login form did not appear after clicking Make Appointment"

        self.logger.info("Clicking the menu toggle to open the menu")
        menu_component.open_menu()

        self.logger.info("Verifying correct menu options showing after logout")
        menu_component.verify_menu_options_for_guest()

        self.logger.info("TC-009 - The test passed successfully")


    def test_menu_logout(self):
        # Initialize page objects
        home_page = HomePage(self.driver)
        menu_component = MenuComponent(self.driver)

        self.logger.info("Starting TC-008: Verify the user can logout from the menu.")

        # Clicking the Make Appointment button to display the login form
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info(f"Logging in with username {self.username} and password {self.password}")
        appointment_page = login_page.login(self.username, self.password)
        appointment_page.verify_appointment_form_visible()
        self.logger.info("The user is logged in successfully")

        self.logger.info("Opening the menu")
        menu_component.open_menu()

        self.logger.info("Clicking the menu Logout option")
        menu_component.click_menu_logout_option()

        self.logger.info("Waiting for the home page to complete loading")
        self.wait_for_url("https://katalon-demo-cura.herokuapp.com/")

        # Clicking the Make Appointment button to verify the user successfully logged out
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info("Verifying login form is displayed with username, password field and the login button")
        assert login_page.check_login_form_visible(), "Login form did not appear after clicking Make Appointment"

        self.logger.info("Clicking the menu toggle to open the menu")
        menu_component.open_menu()

        self.logger.info("Verifying correct menu options showing after logout")
        menu_component.verify_menu_options_for_guest()
        self.logger.info("TC-008 - The test passed successfully")

