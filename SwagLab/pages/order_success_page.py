from selenium.webdriver.common.by import By

class OrderSuccessPage:

    back_home_button = (By.CSS_SELECTOR, "button#back-to-products")
    order_delivery_message = (By.CSS_SELECTOR, "div.complete-text")
    thank_you_message = (By.CSS_SELECTOR, "h2.complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_thank_you_message(self):
        return self.driver.find_element(*self.thank_you_message).text

    def get_order_delivery_message(self):
        return self.driver.find_element(*self.order_delivery_message).text

    def click_back_home_button(self):
        self.driver.find_element(*self.back_home_button).click()