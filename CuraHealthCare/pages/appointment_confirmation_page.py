from utils.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppointmentConfirmationPage(BaseClass):

    appointment_confirmation_message = (By.CSS_SELECTOR, "#summary .col-xs-12.text-center")
    facility = (By.XPATH, "//p[@id='facility']")
    hospital_readmission = (By.XPATH, "//p[@id='hospital_readmission']")
    health_care_program = (By.XPATH, "//p[@id='program']")
    visit_date = (By.XPATH, "//p[@id='visit_date']")
    comment = (By.XPATH, "//p[@id='comment']")

    def __init__(self, driver):
        self.driver = driver

    def verify_appointment_confirmation_page_displayed(self):
        confirmation_text = self.wait_for_element_visibility(self.appointment_confirmation_message).text
        assert "summary" in self.driver.current_url
        assert "appointment has been booked" in confirmation_text

    def verify_correct_facility(self, facility):
        assert facility == self.driver.find_element(*self.facility).text.strip(), "Facility does not match"

    def verify_hospital_readmission_correct(self, hospital_readmission):
        assert hospital_readmission == self.driver.find_element(*self.hospital_readmission).text.strip(), "Hospital readmission value does not match"

    def verify_correct_healthcare_program(self, health_care_program):
        assert health_care_program == self.driver.find_element(*self.health_care_program).text.strip(), "Healthcare program does not match"

    def verify_correct_visit_date(self, visit_date):
        expected_date = self.driver.find_element(*self.visit_date).text.strip()
        assert visit_date == expected_date, f"Visit date does not match. Expected {visit_date}, Actual {expected_date}."

    def verify_correct_comment(self, comment):
        assert comment == self.driver.find_element(*self.comment).text.strip(), "Comment does not match"
