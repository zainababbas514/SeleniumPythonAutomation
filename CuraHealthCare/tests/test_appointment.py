import pytest
from pages.menu_component import MenuComponent
from pages.home_page import HomePage
from utils.base_class import BaseClass

@pytest.mark.usefixtures("init_browser")
class TestAppointment(BaseClass):

    logger = BaseClass.get_logger()

    # Login Credentials
    creds = BaseClass.get_data_from_json("credentials.json")
    username = creds['login_credentials']['username']
    password = creds['login_credentials']['password']

    # Test Data
    data = BaseClass.get_data_from_json("book_appointment_data.json")

    def test_book_appointment(self):
        self.logger.info("Starting TC-006: Verify the user can book an appointment successfully.")

        # Initialize page objects
        home_page = HomePage(self.driver)

        facility = self.data['TC-006']['appointment_form_data']['facility']
        hospital_readmission = self.data['TC-006']['appointment_form_data']['hospital_readmission']
        health_care_program = self.data['TC-006']['appointment_form_data']['healthcare_program']
        visit_date = self.data['TC-006']['appointment_form_data']['visit_date']
        comment = self.data['TC-006']['appointment_form_data']['comment']

        # Clicking the Make Appointment button to display the login form
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info(f"The user is logging in with username {self.username} and password {self.password}")
        appointment_page = login_page.login(self.username, self.password)
        appointment_page.verify_appointment_form_visible()
        self.logger.info("The user is logged in successfully")

        self.logger.info(f"Selecting {facility} facility from the dropdown")
        appointment_page.select_facility(facility)

        self.logger.info("Clicking Apply for hospital readmission")
        appointment_page.apply_hospital_readmission(hospital_readmission)

        self.logger.info(f"Clicking {health_care_program} healthcare program radio button")
        appointment_page.choose_healthcare_programs(health_care_program)

        self.logger.info(f"Selecting {visit_date} as visit date")
        appointment_page.select_visit_date(visit_date)

        self.logger.info(f"Writing comment in the comment box")
        appointment_page.write_comment(comment)

        self.logger.info("Submitting the book appointment form")
        appointment_confirmation_page = appointment_page.click_appointment_button()

        self.logger.info(f"Verifying {facility} facility is selected")
        appointment_confirmation_page.verify_correct_facility(facility)

        self.logger.info(f"Verifying hospital readmission is {hospital_readmission}")
        appointment_confirmation_page.verify_hospital_readmission_correct(hospital_readmission)

        self.logger.info(f"Verifying {health_care_program} healthcare program is selected")
        appointment_confirmation_page.verify_correct_healthcare_program(health_care_program)

        self.logger.info(f"Verifying {visit_date} as visit date is selected")
        appointment_confirmation_page.verify_correct_visit_date(visit_date)

        self.logger.info(f"Verifying comment in the comment box")
        appointment_confirmation_page.verify_correct_comment(comment)

    def test_book_appointment_in_history(self):
        self.logger.info("Starting TC-007: Verify the booked appointment appears in the History with correct details.")

        # Initialize page objects
        home_page = HomePage(self.driver)
        menu_component = MenuComponent(self.driver)

        facility = self.data['TC-007']['appointment_form_data']['facility']
        hospital_readmission = self.data['TC-007']['appointment_form_data']['hospital_readmission']
        health_care_program = self.data['TC-007']['appointment_form_data']['healthcare_program']
        visit_date = self.data['TC-007']['appointment_form_data']['visit_date']
        comment = self.data['TC-007']['appointment_form_data']['comment']

        # Clicking the Make Appointment button to display the login form
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info(f"The user is logging in with username {self.username} and password {self.password}")
        appointment_page = login_page.login(self.username, self.password)
        appointment_page.verify_appointment_form_visible()
        self.logger.info("The user is logged in successfully")

        self.logger.info(f"Selecting {facility} facility from the dropdown")
        appointment_page.select_facility(facility)

        self.logger.info("Clicking Apply for hospital readmission")
        appointment_page.apply_hospital_readmission(hospital_readmission)

        self.logger.info(f"Clicking {health_care_program} healthcare program radio button")
        appointment_page.choose_healthcare_programs(health_care_program)

        self.logger.info(f"Selecting {visit_date} as visit date")
        appointment_page.select_visit_date(visit_date)

        self.logger.info(f"Writing comment in the comment box")
        appointment_page.write_comment(comment)

        self.logger.info("Submitting the book appointment form")
        appointment_confirmation_page = appointment_page.click_appointment_button()

        self.logger.info("Verifying appointment booked successfully")
        appointment_confirmation_page.verify_appointment_confirmation_page_displayed()

        self.logger.info(f"Verifying {facility} facility is selected")
        appointment_confirmation_page.verify_correct_facility(facility)

        self.logger.info(f"Verifying hospital readmission is {hospital_readmission}")
        appointment_confirmation_page.verify_hospital_readmission_correct(hospital_readmission)

        self.logger.info(f"Verifying {health_care_program} healthcare program is selected")
        appointment_confirmation_page.verify_correct_healthcare_program(health_care_program)

        self.logger.info(f"Verifying {visit_date} as visit date is selected")
        appointment_confirmation_page.verify_correct_visit_date(visit_date)

        self.logger.info(f"Verifying comment in the comment box")
        appointment_confirmation_page.verify_correct_comment(comment)

        self.logger.info("Clicking the menu toggle to open the menu")
        menu_component.open_menu()

        self.logger.info("Clicking the 'History' option from the menu")
        history_page = menu_component.click_menu_history_option()

        self.logger.info("Verifying the History page is loaded successfully")
        history_page.verify_history_page_displayed()

        self.logger.info(f"Verifying correct {visit_date} date is showing as panel heading in the History page")
        history_page.verify_correct_visit_date(visit_date)

        self.logger.info(f"Verifying correct {facility} facility is showing inside the History panel")
        history_page.verify_correct_facility(facility)

        self.logger.info(f"Verifying hospital readmission is {hospital_readmission}")
        history_page.verify_hospital_readmission_correct(hospital_readmission)

        self.logger.info(f"Verifying {health_care_program} healthcare program is selected")
        history_page.verify_correct_healthcare_program(health_care_program)

        self.logger.info(f"Verifying correct comment is showing")
        history_page.verify_correct_comment(comment)

    def test_visit_date_is_required(self):
        self.logger.info("Starting TC-010: Verify the make appointment form cannot be submitted without selecting a Visit Date.")

        # Initialize page objects
        home_page = HomePage(self.driver)

        # Clicking the Make Appointment button to display the login form
        self.logger.info("Clicking the 'Make Appointment' button")
        login_page = home_page.click_book_appointment_button()

        self.logger.info(f"The user is logging in with username {self.username} and password {self.password}")
        appointment_page = login_page.login(self.username, self.password)
        appointment_page.verify_appointment_form_visible()
        self.logger.info("The user is logged in successfully")

        self.logger.info("Submitting the book appointment form without entering Visit Date")
        appointment_page.click_appointment_button()

        self.logger.info("Verifying the user is still on the appointment page")
        appointment_page.verify_appointment_form_visible()

        self.logger.info("Verifying the datepicker is displayed")
        appointment_page.verify_datepicker_visible()

        self.logger.info("Verifying 'Please fill in this field' tooltip is shown below the visit date")
        appointment_page.verify_visit_date_required_message_visible()























