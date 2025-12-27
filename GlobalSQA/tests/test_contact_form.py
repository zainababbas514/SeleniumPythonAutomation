import pytest
from utils.BaseClass import BaseClass
from pages.practice_component_page import PracticeComponentPage

@pytest.mark.usefixtures("browser_setup")
class TestContactForm(BaseClass):
    logger = BaseClass.get_logger()

    def test_contact_form(self):
        # Initialize page objects
        components_page = PracticeComponentPage(self.driver)

        # Test Data
        data = BaseClass.get_test_data("TC-010", "ContactForm")[0]

        name = data['Name']
        email = data['Email']
        website = data['Website']
        experience = data['Experience']
        education = data['Education']
        comments = data['Comments']
        first_alert_text = data['FirstAlertText']
        second_alert_text = data['SecondAlertText']
        form_success_message = data['SuccessMessage']
        expertise = data['Expertise']

        self.logger.info("Starting TC-010: Verify the contact form submits correctly.")

        self.logger.info("Opening Sample Page Test page")
        contact_form_page = components_page.open_contact_form_page()

        self.logger.info("Waiting for the Sample Page to load")
        self.wait_for_page_load("samplepagetest/", contact_form_page.contact_form)

        self.logger.info("Filling the contact form")
        contact_form_page.fill_contact_form(data)

        self.logger.info("Clicking Alert Button")
        contact_form_page.click_alert_button()

        self.logger.info("Handling first alert")
        contact_form_page.handle_alert(first_alert_text)

        self.logger.info("Handling second alert")
        contact_form_page.handle_alert(second_alert_text)

        self.logger.info("Verifying form submitted")
        success_message = contact_form_page.get_success_message()
        assert success_message.is_displayed()
        assert success_message.text == form_success_message

        self.logger.info("Verifying submitted form details")
        assert contact_form_page.get_submitted_name() == name, "Name mismatch after submission"
        assert contact_form_page.get_submitted_email() == email, "Email mismatch after submission"
        assert contact_form_page.get_submitted_website() == website, "Website mismatch after submission"
        assert contact_form_page.get_submitted_experience() == experience, "Experience mismatch after submission"
        assert contact_form_page.get_selected_expertise() == expertise, "Expertise mismatch after submission"
        assert contact_form_page.get_submitted_comment() == comments, "Comment mismatch after submission"
        assert contact_form_page.get_selected_education() == education, "Education mismatch after submission"
