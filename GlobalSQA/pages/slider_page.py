from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils.BaseClass import BaseClass

class SliderPage(BaseClass):
    range_tab = (By.XPATH, '//li[@id="Range"]')
    iframe = (By.XPATH, "(//iframe[@class='demo-frame'])[2]")
    sliders = (By.CSS_SELECTOR, "#slider-range .ui-slider-handle")
    range_slider = (By.CSS_SELECTOR, "#slider-range.ui-slider")
    price_range_input = (By.XPATH, "//input[@id='amount']")

    def __init__(self, driver):
        self.driver = driver

    def get_min_price_handle(self):
        return self.driver.find_elements(*self.sliders)[0]

    def get_max_price_handle(self):
        return self.driver.find_elements(*self.sliders)[1]

    def get_range_slider(self):
        return self.driver.find_element(*self.range_slider)

    def set_slider_value(self, handle, value, max_value):
        self.wait_for_element_visibility(self.range_slider)
        actions = ActionChains(self.driver)

        # Real slider width in pixels
        width = self.get_range_slider().size['width']

        # How many pixels represent 1 value unit
        pixels_per_value = width / max_value

        # Where the handle SHOULD be (in pixels)
        target_pixel_position = value * pixels_per_value

        # Where the handle CURRENTLY is (in % → convert to px)
        current_percent = float(handle.get_attribute("style").split(":")[1].strip("%; "))
        current_pixel_position = (current_percent / 100) * width

        # How much to drag
        drag_offset = round(target_pixel_position - current_pixel_position)

        # Drag and drop
        actions.click_and_hold(handle).move_by_offset(drag_offset, 0).release().perform()

    def get_price_range(self):
        return self.driver.find_element(*self.price_range_input).get_attribute('value')


