import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.base_class import BaseClass
from pages.menu_component import MenuComponent

@pytest.mark.usefixtures("init_browser")
class TestLogin(BaseClass):

    logger = BaseClass.get_logger()

    def test_make_appointment_shows_login_form(self):
        self.logger.info("Starting TC-001: Verify login form becomes visible when clicking 'Make Appointment' button.")

        # Initialize page objects
        home_page = HomePage(self.driver)

        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info("Verifying login form is displayed with username, password field and the login button")
        assert login_page.check_login_form_visible(), "Login form did not appear after clicking Make Appointment"
        self.logger.info("TC-001 Passed: The login form is visible with all fields and the login button")

    def test_menu_login_option_shows_login_form(self):
        self.logger.info("Starting TC-002: Verify clicking the 'Login' option from the menu displays the login form.")

        # Initialize the page objects
        login_page = LoginPage(self.driver)
        menu_component = MenuComponent(self.driver)

        self.logger.info("Clicking the menu toggle to open the menu")
        menu_component.open_menu()

        self.logger.info("Clicking the 'Login' option from the menu")
        menu_component.click_menu_login_option()

        self.logger.info("Verifying login form is displayed with username, password field and the login button")
        assert login_page.check_login_form_visible(), "Login form did not appear after clicking the Login option from the menu"
        self.logger.info("TC-002 Passed: The login form is visible with all fields and the login button")


    @pytest.mark.parametrize("credentials", (BaseClass.get_data_from_json("login_test_data.json").values()))
    def test_login(self, credentials):

            # Initialize page objects
            home_page = HomePage(self.driver)

            self.logger.info("Clicking the 'Make Appointment' button")
            login_page = home_page.click_book_appointment_button()

            self.logger.info(f"Logging in with username {credentials['username']} and password {credentials['password']}")
            appointment_page = login_page.login(credentials["username"], credentials["password"])
            if credentials["expected_result"] != "success":
                login_page.verify_failed_login()
                self.logger.info(f"Login failed with invalid credentials")
            else:
                appointment_page.verify_appointment_form_visible()
                self.logger.info(f"The user is logged in successfully with valid credentials")
