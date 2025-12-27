from selenium.webdriver.common.by import By
from utils.base_class import BaseClass

class HistoryPage(BaseClass):

    history_page_heading = (By.XPATH, "//h2[normalize-space()='History']")
    panel_heading = (By.XPATH, "(//div[@class='panel-heading'])[1]")
    facility = (By.XPATH, "(//p[@id='facility'])[1]")
    hospital_readmission = (By.XPATH, "(//p[@id='hospital_readmission'])[1]")
    health_care_program = (By.XPATH, "(//p[@id='program'])[1]")
    comment = (By.XPATH, "(//p[@id='comment'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def verify_history_page_displayed(self):
        self.wait_for_element_visibility(self.history_page_heading)
        heading = self.driver.find_element(*self.history_page_heading).text
        assert 'History' == heading.strip()
        assert 'history' in self.driver.current_url

    def verify_correct_facility(self, facility):
        assert facility == self.driver.find_element(*self.facility).text.strip(), "Facility does not match"

    def verify_hospital_readmission_correct(self, hospital_readmission):
        assert hospital_readmission == self.driver.find_element(*self.hospital_readmission).text.strip(), "Hospital readmission value does not match"

    def verify_correct_healthcare_program(self, health_care_program):
        assert health_care_program == self.driver.find_element(*self.health_care_program).text.strip(), "Healthcare program does not match"

    def verify_correct_visit_date(self, visit_date):
        assert visit_date == self.driver.find_element(*self.panel_heading).text.strip(), "Visit date does not match"

    def verify_correct_comment(self, comment):
        assert comment == self.driver.find_element(*self.comment).text.strip(), "Comment does not match"
