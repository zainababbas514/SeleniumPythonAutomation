from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils.BaseClass import BaseClass

class TooltipPage(BaseClass):
    forms_based_tab = (By.XPATH, "//li[@id='Forms Based']")
    first_name_input = (By.XPATH, "//input[@id='firstname']")
    last_name_input = (By.XPATH, "//input[@id='lastname']")
    address = (By.XPATH, "//input[@id='address']")
    page_heading = (By.CSS_SELECTOR, "div.sixteen .page_heading")
    iframe = (By.XPATH, "//div[@rel-title='Forms Based']//iframe")
    tooltip_text = (By.CSS_SELECTOR, ".ui-tooltip-content")

    def __init__(self, driver):
        self.driver = driver

    def get_input_field(self, locator):
        return self.driver.find_element(*locator)

    def get_tooltip(self, tooltip_id):
        return self.driver.find_element(By.CSS_SELECTOR, f"#{tooltip_id}")

    def get_tooltip_text(self, tooltip_id):
        return self.get_tooltip(tooltip_id).find_element(*self.tooltip_text).text.strip()

    def hover_over_input_field(self, locator):
        element = self.get_input_field(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return element.get_attribute('aria-describedby')

    def verify_tooltip_text(self, tooltip_id, expected_text):
        assert self.get_tooltip(tooltip_id).is_displayed()
        tooltip_text = self.get_tooltip_text(tooltip_id)
        assert tooltip_text == expected_text








