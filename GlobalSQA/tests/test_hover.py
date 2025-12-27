import pytest
from pages.practice_component_page import PracticeComponentPage
from utils.BaseClass import BaseClass

@pytest.mark.usefixtures("browser_setup")
class TestHover(BaseClass):
    logger = BaseClass.get_logger()

    def test_input_hover_shows_tooltip(self):
        # Initialize page objects
        components_page = PracticeComponentPage(self.driver)

        # Test Data
        data = BaseClass.get_test_data("TC-005", "Tooltips")[0]

        self.logger.info("Starting TC-005: Verify hovering over the input fields displays the appropriate tooltip")

        self.logger.info("Opening Tooltip page")
        tooltip_page = components_page.open_tooltip_page()

        self.logger.info("Waiting for the Tooltip page to load completely")
        self.wait_for_page_load("tooltip/", tooltip_page.page_heading)
        self.open_tab(tooltip_page.forms_based_tab)

        self.logger.info("Switching inside the form iframe")
        self.switch_to_frame(tooltip_page.iframe)

        self.logger.info("Hovering over First Name input")
        fields = {
            "First Name": (tooltip_page.first_name_input, data['FirstNameTooltip']),
            "Last Name": (tooltip_page.last_name_input, data['LastNameTooltip']),
            "Address": (tooltip_page.address, data['AddressTooltip'])
        }
        for label, (locator, expected_tooltip) in fields.items():
            self.logger.info(f"Hovering over {label} input")
            tooltip_id = tooltip_page.hover_over_input_field(locator)

            self.logger.info(f"Verifying {label} tooltip displayed with the correct text")
            tooltip_page.verify_tooltip_text(tooltip_id, expected_tooltip)

        self.driver.switch_to.default_content()

