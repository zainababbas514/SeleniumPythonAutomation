from selenium.webdriver.common.by import By
from utils.BaseClass import BaseClass

class ProgressBarPage(BaseClass):
    main_container = (By.XPATH, "//div[@rel-title='Download Manager']")
    download_button = (By.XPATH, "//button[@id='downloadButton']")
    dialog_button = (By.XPATH, "//div[@class='ui-dialog-buttonset']//button")
    progress_bar = (By.CSS_SELECTOR, "#progressbar div.ui-progressbar-value")
    progress_label = (By.CSS_SELECTOR, "#dialog .progress-label")
    iframe = (By.XPATH, "(//iframe[@class='demo-frame'])[1]")
    progress_bar_dialog = (By.CSS_SELECTOR, "div.ui-dialog")

    def __init__(self, driver):
        self.driver = driver

    def get_download_button(self):
        return self.driver.find_element(*self.download_button)

    def click_download_button(self):
        download_button = self.get_download_button()
        download_button.click()

    def get_progress_label_text(self):
        return self.driver.find_element(*self.progress_label).text

    def get_dialog_box_button(self):
        return self.driver.find_element(*self.dialog_button)

    def click_progress_dialog_button(self):
        dialog_button = self.get_dialog_box_button()
        self.driver.execute_script("arguments[0].click();", dialog_button)

    def get_progress_bar_dialog(self):
        return self.driver.find_element(*self.progress_bar_dialog)



