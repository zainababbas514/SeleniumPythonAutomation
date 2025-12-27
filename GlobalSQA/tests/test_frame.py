import pytest
from pages.practice_component_page import PracticeComponentPage
from utils.BaseClass import BaseClass

@pytest.mark.usefixtures("browser_setup")
class TestFrame(BaseClass):
    logger = BaseClass.get_logger()

    def test_training_inside_iframe_opens(self):
        # Initialize page objects
        components_page = PracticeComponentPage(self.driver)

        self.logger.info("Starting TC-004: Verify clicking the “Click Here” button from the Open New Tab option opens a new tab successfully")

        self.logger.info("Opening Frames page")
        # self.close_any_ads()
        frames_page = components_page.open_frames_page()

        self.logger.info("Waiting for the Frames page to load completely")
        self.wait_for_page_load("frames-and-windows/", frames_page.tabs_container)
        self.open_tab(frames_page.open_iframe_tab_option)

        self.logger.info("Switching to the trainings iframe")
        self.switch_to_frame(frames_page.trainings_iframe)

        heading = frames_page.open_a_random_training()
        self.logger.info(f"Opened random training: {heading}")

        self.wait_for_element_visibility(frames_page.training_page_container)
        training_page_heading = frames_page.get_training_page_heading()
        self.logger.info("Verifying the correct training opened")
        assert heading == training_page_heading, f"Expected {heading} to open, but {training_page_heading} training opened"

        self.driver.switch_to.default_content()



