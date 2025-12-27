import time

import pytest
from utils.BaseClass import BaseClass
from pages.practice_component_page import PracticeComponentPage

@pytest.mark.usefixtures("browser_setup")
class TestHover(BaseClass):
    logger = BaseClass.get_logger()

    @pytest.mark.parametrize("reorder_data", BaseClass.get_test_data("TC-008", "Reorder"))
    def test_reordering_list(self, reorder_data):
        components_page = PracticeComponentPage(self.driver)

        self.logger.info("Starting TC-008: Verify re-ordering items in the list reflects the correct order")

        self.logger.info("Opening Sorting page")
        sorting_page = components_page.open_sorting_page()

        self.logger.info("Open the Simple list tab")
        self.open_tab(sorting_page.simple_list_tab)

        self.logger.info("Switching inside the form iframe")
        self.switch_to_frame(sorting_page.iframe)

        self.logger.info(f"Reordering {reorder_data['MoveItem']} on the position of {reorder_data['DropBefore']}")
        sorting_page.reorder_item(reorder_data['MoveItem'], reorder_data['DropBefore'])

        self.logger.info("Verifying order is correct")
        sorting_page.verify_list_order(reorder_data['ExpectedOrder'])

        self.driver.switch_to.default_content()





