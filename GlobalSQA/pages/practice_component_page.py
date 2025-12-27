from pages.contact_form_page import ContactFormPage
from pages.frames_page import FramesPage
from pages.progress_bar_page import ProgressBarPage
from pages.slider_page import SliderPage
from pages.sorting_page import SortingPage
from pages.tooltip_page import TooltipPage
from selenium.webdriver.common.by import By
from pages.drag_drop_page import DragDropPage
from pages.auto_complete_page import AutoCompletePage

class PracticeComponentPage:
    drag_drop_option = (By.XPATH, "//a[normalize-space()='DragAndDrop']")
    frames_option = (By.XPATH, "//a[normalize-space()='Frames']")
    tooltip_option = (By.XPATH, "//a[normalize-space()='ToolTip']")
    auto_complete_option = (By.XPATH, "//a[normalize-space()='AutoComplete']")
    progress_bar_option = (By.XPATH, "//a[normalize-space()='ProgressBar']")
    sorting_option = (By.XPATH, "//a[normalize-space()='Sorting']")
    slider_option = (By.XPATH, "//a[normalize-space()='Slider']")
    sample_page_option = (By.XPATH, "//a[normalize-space()='SamplePage']")

    def __init__(self, driver):
        self.driver = driver

    def open_drag_drop_page(self):
        drag_drop_option = self.driver.find_element(*self.drag_drop_option)
        self.driver.execute_script("arguments[0].click()", drag_drop_option)
        return DragDropPage(self.driver)

    def open_frames_page(self):
        frames_options = self.driver.find_element(*self.frames_option)
        self.driver.execute_script("arguments[0].click()", frames_options)
        return FramesPage(self.driver)

    def open_tooltip_page(self):
        tooltip_option = self.driver.find_element(*self.tooltip_option)
        self.driver.execute_script("arguments[0].click()", tooltip_option)
        return TooltipPage(self.driver)

    def open_auto_complete_page(self):
        auto_complete_option = self.driver.find_element(*self.auto_complete_option)
        self.driver.execute_script("arguments[0].click()", auto_complete_option)
        return AutoCompletePage(self.driver)

    def open_sorting_page(self):
        sorting_option = self.driver.find_element(*self.sorting_option)
        self.driver.execute_script("arguments[0].click()", sorting_option)
        return SortingPage(self.driver)

    def open_contact_form_page(self):
        sample_page_option = self.driver.find_element(*self.sample_page_option)
        self.driver.execute_script("arguments[0].click()", sample_page_option)
        return ContactFormPage(self.driver)

    def open_slider_page(self):
        slider_option = self.driver.find_element(*self.slider_option)
        self.driver.execute_script("arguments[0].click()", slider_option)
        return SliderPage(self.driver)

    def open_progress_bar_page(self):
        progress_bar_option = self.driver.find_element(*self.progress_bar_option)
        self.driver.execute_script("arguments[0].click()", progress_bar_option)
        return ProgressBarPage(self.driver)




