import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.base_class import BaseClass
from pages.appointment_confirmation_page import AppointmentConfirmationPage

class AppointmentPage(BaseClass):

    appointment_section = (By.CSS_SELECTOR, 'section#appointment')
    facility_dropdown = (By.XPATH, "//select[@id='combo_facility']")
    hospital_readmission_checkbox = (By.XPATH, "//input[@name='hospital_readmission']")
    comment_box = (By.XPATH, "//textarea[@id='txt_comment']")
    book_appointment_button = (By.XPATH, "//button[@id='btn-book-appointment']")
    visit_date_input = (By.XPATH, "//input[@id='txt_visit_date']")
    datepicker = (By.CSS_SELECTOR, ".datepicker.datepicker-dropdown")
    datepicker_switch = (By.CSS_SELECTOR, ".datepicker .datepicker-days .datepicker-switch")
    year = (By.CSS_SELECTOR, ".datepicker .datepicker-months .datepicker-switch")
    datepicker_months_table = (By.CSS_SELECTOR, ".datepicker .datepicker-months")
    year_prev_button = (By.CSS_SELECTOR, ".datepicker-months .prev")
    year_next_button = (By.CSS_SELECTOR, ".datepicker-months .next")
    months = (By.CSS_SELECTOR, ".datepicker-months .month")
    days = (By.CSS_SELECTOR, ".datepicker-days .day")

    def __init__(self, driver):
        self.driver = driver

    def verify_appointment_form_visible(self):
        self.wait_for_element_visibility(self.appointment_section)
        assert "appointment" in self.driver.current_url

    def select_facility(self, facility):
        dropdown = Select(self.driver.find_element(*self.facility_dropdown))
        dropdown.select_by_value(facility)

    def apply_hospital_readmission(self, value):
        if value == "Yes":
            hospital_readmission_checkbox = (self.driver.find_element(*self.hospital_readmission_checkbox))
            hospital_readmission_checkbox.click()
            assert hospital_readmission_checkbox.is_selected()

    def get_healthcare_program_radio(self, value):
        return self.driver.find_element(By.XPATH, f"//input[@value='{value}']")

    def choose_healthcare_programs(self, value):
        healthcare_program_radio = self.get_healthcare_program_radio(value)
        healthcare_program_radio.click()
        assert healthcare_program_radio.is_selected(), "The specified healthcare program radio button is not checked"

    def select_visit_date(self, visit_date):

        # Parse the date string
        parsed = datetime.strptime(visit_date, "%d/%m/%Y")
        year = str(parsed.year)
        expected_month = parsed.strftime("%b")
        expected_day = str(parsed.day)

        self.driver.find_element(*self.visit_date_input).click()
        assert self.driver.find_element(*self.datepicker).is_displayed()

        self.driver.find_element(*self.datepicker_switch).click()
        assert self.driver.find_element(*self.datepicker_months_table).is_displayed()

        # Select Year
        selected_year = self.driver.find_element(*self.datepicker_months_table)
        text = selected_year.find_element(*self.year).text
        while text != year:
            self.driver.find_element(*self.year_next_button).click()
            text = selected_year.find_element(*self.year).text

        # Select Month
        months_list = self.driver.find_elements(*self.months)
        for month in months_list:
            if month.text == expected_month:
                month.click()
                break

        # Select Day
        days_list = self.driver.find_elements(*self.days)
        for day in days_list:
            if day.text == expected_day and "old" not in day.get_attribute("class"):
                day.click()
                break

    def write_comment(self, text):
        self.driver.find_element(*self.comment_box).send_keys(text)

    def click_appointment_button(self):
        self.driver.find_element(*self.book_appointment_button).click()
        return AppointmentConfirmationPage(self.driver)

    def verify_datepicker_visible(self):
        date_picker = self.driver.find_element(*self.datepicker)
        assert date_picker.is_displayed()

    def verify_visit_date_required_message_visible(self):
        element = self.driver.find_element(*self.visit_date_input)
        is_valid = self.driver.execute_script("return arguments[0].checkValidity();", element)
        message = self.driver.execute_script("return arguments[0].validationMessage;", element)

        assert is_valid is False, "Visit Date field is incorrectly marked as valid."
        assert "please fill out this field" in message.lower(), f"Unexpected validation message: {message}"
