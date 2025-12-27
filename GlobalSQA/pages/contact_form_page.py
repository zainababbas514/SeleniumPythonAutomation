from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.BaseClass import BaseClass

class ContactFormPage(BaseClass):

    contact_form = (By.CSS_SELECTOR, "#contact-form-2599")
    profile_picture_input = (By.XPATH, "//input[@class='wpcf7-form-control wpcf7-file']")
    name_input = (By.XPATH, "//input[@id='g2599-name']")
    email_input = (By.XPATH, "//input[@id='g2599-email']")
    website_input = (By.XPATH, "//input[@id='g2599-website']")
    experience_dropdown = (By.XPATH, "//select[@id='g2599-experienceinyears']")
    expertise_checkbox_list = (By.CSS_SELECTOR, ".checkbox-multiple.grunion-field")
    education_radio_list = (By.CSS_SELECTOR, ".grunion-radio-options .contact-form-field input")
    alert_button = (By.XPATH, "//button[normalize-space()='Alert Box : Click Here']")
    comment_textarea = (By.XPATH, "//textarea[@name='g2599-comment']")
    submit_button = (By.XPATH, "//button[@class='pushbutton-wide']")
    contact_form_success_message = (By.XPATH, "//h4[@id='contact-form-success-header']")

    # Locators for submitted values
    submitted_name = (By.XPATH, "//div[normalize-space()='Name:']/following-sibling::div[1]")
    submitted_email = (By.XPATH, "//div[normalize-space()='Email:']/following-sibling::div[1]")
    submitted_website = (By.XPATH, "//div[normalize-space()='Website:']/following-sibling::div[1]")
    selected_experience = (By.XPATH, "//div[normalize-space()='Experience (In Years):']/following-sibling::div[1]")
    submitted_comment = (By.XPATH, "//div[normalize-space()='Comment:']/following-sibling::div[1]")
    selected_education = (By.XPATH, "//div[normalize-space()='Education:']/following-sibling::div[1]")
    selected_expertise = (By.XPATH, "//div[normalize-space()='Expertise :']/following-sibling::div[1]")

    def __init__(self, driver):
        self.driver = driver

    def upload_profile_picture(self, url):
        profile_picture = self.driver.find_element(*self.profile_picture_input)
        profile_picture.send_keys(url)

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_website(self, website):
        self.driver.find_element(*self.website_input).send_keys(website)

    def select_experience(self, experience):
        experience_dropdown = Select(self.driver.find_element(*self.experience_dropdown))
        experience_dropdown.select_by_value(experience)

    def select_expertise(self, expertise):
        checkbox_list = self.driver.find_elements(*self.expertise_checkbox_list)
        for checkbox in checkbox_list:
            if checkbox.get_attribute('value') == expertise.strip():
                checkbox.click()
                break

    def select_education(self, education):
        radio_list = self.driver.find_elements(*self.education_radio_list)
        for radio in radio_list:
            if radio.get_attribute('value') == education:
                radio.click()
                break

    def click_alert_button(self):
        alert_button = self.driver.find_element(*self.alert_button)
        self.driver.execute_script("arguments[0].click()", alert_button)

    def handle_alert(self, expected_text):
        alert_text = self.accept_alert()
        assert alert_text == expected_text

    def write_comment(self, comment):
        self.driver.find_element(*self.comment_textarea).send_keys(comment)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self):
        success_message = self.driver.find_element(*self.contact_form_success_message)
        return success_message

    def get_submitted_name(self):
        return self.driver.find_element(*self.submitted_name).text

    def get_submitted_email(self):
        return self.driver.find_element(*self.submitted_email).text

    def get_submitted_website(self):
        return self.driver.find_element(*self.submitted_website).text

    def get_submitted_experience(self):
        return self.driver.find_element(*self.selected_experience).text

    def get_submitted_comment(self):
        return self.driver.find_element(*self.submitted_comment).text

    def get_selected_education(self):
        return self.driver.find_element(*self.selected_education).text

    def get_selected_expertise(self):
        return self.driver.find_element(*self.selected_expertise).text

    def fill_contact_form(self, data):
        self.upload_profile_picture(data['ProfilePicture'])
        self.enter_name(data['Name'])
        self.enter_email(data['Email'])
        self.enter_website(data['Website'])
        for exp in data['Expertise'].split(","):
            self.select_expertise(exp)
        self.select_experience(data['Experience'])
        self.select_education(data['Education'])
        self.write_comment(data['Comments'])

