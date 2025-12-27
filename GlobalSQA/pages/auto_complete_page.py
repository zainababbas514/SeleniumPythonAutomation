from selenium.webdriver.common.by import By
from utils.BaseClass import BaseClass

class AutoCompletePage(BaseClass):

    categories_tab = (By.XPATH, "//li[@id='Categories']")
    combobox_tab = (By.XPATH, "//li[@class='ComboBox']")
    iframe = (By.XPATH, "(//iframe[@class='demo-frame'])[1]")
    search_input = (By.XPATH, "//input[@id='search']")
    page_heading = (By.CSS_SELECTOR, "div.sixteen .page_heading")
    search_result = (By.CSS_SELECTOR, ".ui-autocomplete .ui-menu-item .ui-menu-item-wrapper")

    def __init__(self, driver):
        self.driver = driver

    def search(self, text):
        search_field = self.driver.find_element(*self.search_input)
        search_field.clear()
        search_field.send_keys(text)

    def search_results(self):
        elements = self.wait_for_all_element_visibility(self.search_result)
        return elements

    def verify_search_result_correct(self, searchText):
        search_results = self.search_results()
        search_text_lower = searchText.lower()

        assert search_results, "No search results appeared!"

        for item in search_results:
            item_text = item.text.lower()
            assert search_text_lower in item_text, f"Expected '{searchText}' in result '{item.text}', but it was not found."







