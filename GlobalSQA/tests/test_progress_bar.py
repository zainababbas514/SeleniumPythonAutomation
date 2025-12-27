import time
import pytest
from utils.BaseClass import BaseClass
from selenium.webdriver import ActionChains
from pages.practice_component_page import PracticeComponentPage

@pytest.mark.usefixtures("browser_setup")
class TestProgressBar(BaseClass):
    logger = BaseClass.get_logger()

    def test_progress_bar(self):
        components_page = PracticeComponentPage(self.driver)

        self.logger.info("Starting TC-007: Verify the progress bar functionality.")

        self.logger.info("Opening Progress Bar page")
        progress_bar_page = components_page.open_progress_bar_page()

        self.logger.info("Waiting for the Progress Bar page")
        self.wait_for_page_load("progress-bar/", progress_bar_page.main_container)

        self.logger.info("Switching inside the form iframe")
        self.switch_to_frame(progress_bar_page.iframe)

        self.logger.info("Clicking Download Button")
        progress_bar_page.click_download_button()

        self.logger.info("Verifying dialog is displayed")
        assert progress_bar_page.get_progress_bar_dialog().is_displayed(), "Dialog did not appear"

        self.logger.info("Verifying Download button disabled with text 'Downloading...'")
        download_btn = progress_bar_page.get_download_button()
        assert not download_btn.is_enabled()
        assert download_btn.text == "Downloading..."

        initial_label_text = progress_bar_page.get_progress_label_text()

        self.logger.info("Verifying Cancel Download button during progress")
        assert "Cancel" in progress_bar_page.get_dialog_box_button().text

        self.logger.info("Waiting for progress to reach Complete!")
        self.wait_for_text_present(progress_bar_page.progress_label, "Complete!")

        final_label_text = progress_bar_page.get_progress_label_text()

        self.logger.info("Verifying dialog button changed to Close")
        assert progress_bar_page.get_dialog_box_button().text == "Close"

        self.logger.info("Verifying progress label changed")
        assert initial_label_text != final_label_text, "Progress did not move or change text"

        self.logger.info("Verifying Download button still disabled")
        assert not progress_bar_page.get_download_button().is_enabled()
        assert progress_bar_page.get_download_button().text == "Downloading..."

        self.logger.info("Clicking Close button")
        progress_bar_page.click_progress_dialog_button()

        self.logger.info("Verifying dialog is now hidden")
        assert self.wait_for_element_invisibility(progress_bar_page.progress_bar_dialog)

        self.logger.info("Verifying Download button re-enabled with correct text")
        download_btn = progress_bar_page.get_download_button()
        assert download_btn.is_enabled()
        assert download_btn.text == "Start Download"

        self.driver.switch_to.default_content()



