import pytest
from utils.BaseClass import BaseClass
from pages.practice_component_page import PracticeComponentPage

@pytest.mark.usefixtures("browser_setup")
class TestDropDown(BaseClass):
    logger = BaseClass.get_logger()

    def test_search_results_correct(self):
        # Initializing page objects
        components_page = PracticeComponentPage(self.driver)

        data = BaseClass.get_test_data("TC-006", "Search")[0]
        search_text = data['SearchText']

        self.logger.info("Opening Auto Complete page")
        auto_complete_page = components_page.open_auto_complete_page()

        self.logger.info("Waiting for page load")
        self.wait_for_page_load("auto-complete/", auto_complete_page.page_heading)
        self.open_tab(auto_complete_page.categories_tab)

        self.logger.info("Switching into iframe")
        self.switch_to_frame(auto_complete_page.iframe)

        self.logger.info(f"Typing '{search_text}' in search box")
        auto_complete_page.search(search_text)

        self.logger.info("Verifying search results")
        auto_complete_page.verify_search_result_correct(search_text)

        self.driver.switch_to.default_content()

