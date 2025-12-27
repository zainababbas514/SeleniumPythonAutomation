from selenium.webdriver.common.by import By
from utils.BaseClass import BaseClass

class FramesPage(BaseClass):

    tabs_container = (By.CSS_SELECTOR, "div.twelve.columns")
    page_heading = (By.CSS_SELECTOR, "div.sixteen .page_heading")
    open_new_tab_option = (By.XPATH, "//li[normalize-space()='Open New Tab']")
    open_iframe_tab_option = (By.XPATH, "//li[normalize-space()='iFrame']")
    click_here_button = (By.CSS_SELECTOR, ".button_hilite.button_pale")
    trainings_iframe = "globalSqa"
    training_list = (By.CSS_SELECTOR, "#portfolio_items .info_item")
    training_heading = (By.CSS_SELECTOR, ".info_desc h3")
    training_page_heading = (By.CSS_SELECTOR, ".page_heading h1")
    training_page_container = (By.CSS_SELECTOR, "div.portfolio_page")

    def __init__(self, driver):
        self.driver = driver


    def click_click_here_button(self):
        click_here_buttons = self.driver.find_elements(*self.click_here_button)
        for btn in click_here_buttons:
            if btn.is_displayed():
                self.driver.execute_script("arguments[0].click()", btn)
                break

    def get_page_heading(self):
        return self.driver.find_element(*self.page_heading).text

    def switch_to_new_tab(self):
        # Get all window handles
        handles = self.driver.window_handles

        # Switch to the child window
        self.driver.switch_to.window(handles[1])
        return handles

    def get_training_list(self):
        return self.driver.find_elements(*self.training_list)

    def open_a_random_training(self):
        random_index = self.generate_random_number(len(self.get_training_list()))
        random_training = self.get_training_list()[random_index]
        self.driver.execute_script("arguments[0].scrollIntoView(true)", random_training)
        heading = random_training.find_element(*self.training_heading).text
        random_training.click()
        return heading

    def get_training_page_heading(self):
        self.wait_for_element_visibility(self.training_page_container)
        heading = self.wait_for_element_visibility(self.training_page_heading)
        return heading.text















