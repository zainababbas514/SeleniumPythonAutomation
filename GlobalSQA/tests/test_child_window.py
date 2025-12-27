import time

import pytest
from pages.practice_component_page import PracticeComponentPage
from utils.BaseClass import BaseClass

@pytest.mark.usefixtures("browser_setup")
class TestChildWindow(BaseClass):

    logger = BaseClass.get_logger()

    def test_new_tab_has_same_content_as_original(self):
        # Initialize page objects
        components_page = PracticeComponentPage(self.driver)

        self.logger.info("Starting TC-003: Verify clicking the “Click Here” button from the Open New Tab option opens a new tab successfully")

        self.logger.info("Opening Frames page")
        # self.close_any_ads()
        frames_page = components_page.open_frames_page()

        self.logger.info("Waiting for the Frames page to load completely")
        self.wait_for_page_load("frames-and-windows/", frames_page.tabs_container)
        self.open_tab(frames_page.open_new_tab_option)

        # Storing current window url
        original_window_url = self.driver.current_url
        original_window_heading = frames_page.get_page_heading()

        self.logger.info("Clicking the Click Here button")
        frames_page.click_click_here_button()

        self.logger.info("Switching to the new opened tab")
        window_handles = frames_page.switch_to_new_tab()

        new_window_url = self.driver.current_url
        new_window_url = new_window_url.split("#")[0]
        new_window_heading = frames_page.get_page_heading()

        self.logger.info("Verify new window is same as the original one")
        assert original_window_url == new_window_url, f"Expected URL '{original_window_url}', but got '{new_window_url}'"
        assert new_window_heading == original_window_heading, f"Expected heading '{original_window_heading}', but got '{new_window_heading}'"

        # Switch to the parent window
        self.driver.switch_to.window(window_handles[0])
















