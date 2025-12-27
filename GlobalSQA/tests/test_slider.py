import time

import pytest
from selenium.webdriver import ActionChains

from utils.BaseClass import BaseClass
from pages.practice_component_page import PracticeComponentPage

@pytest.mark.usefixtures("browser_setup")
class TestSlider(BaseClass):
    logger = BaseClass.get_logger()

    def test_range_slider(self):
        # Initialize page objects
        components_page = PracticeComponentPage(self.driver)

        # Test Data
        data = BaseClass.get_test_data("TC-009", "Slider")[0]

        self.logger.info("Starting TC-009: Verify selecting a price range using the slider works correctly.")

        self.logger.info("Opening Slider page")
        slider_page = components_page.open_slider_page()

        self.logger.info("Waiting for the Sliders page to load completely")
        self.open_tab(slider_page.range_tab)

        self.logger.info("Switching inside the form iframe")
        self.switch_to_frame(slider_page.iframe)

        min_slide_handle = slider_page.get_min_price_handle()
        max_slide_handle = slider_page.get_max_price_handle()

        min_value = data['MinValue']
        max_value = data['MaxValue']
        max_range = data['MaxRange']

        self.logger.info(f"Setting minimum price slider to {min_value}")
        slider_page.set_slider_value(min_slide_handle, min_value, max_range)

        self.logger.info(f"Setting maximum price slider to {max_value}")
        slider_page.set_slider_value(max_slide_handle, max_value, max_range)

        expected_range = f"${min_value} - ${max_value}"
        actual_range = slider_page.get_price_range()

        self.logger.info("Verifying the selected price range.")
        assert expected_range == actual_range, f"Price range mismatch! Expected range {expected_range}, but actual range is {actual_range}"

        self.driver.switch_to.default_content()


