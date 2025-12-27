from selenium.webdriver.common.by import By
from utils.base_class import BaseClass
from pages.order_success_page import OrderSuccessPage

class CheckoutPageTwo(BaseClass):
    checkout_items_list = (By.CSS_SELECTOR, ".cart_list .cart_item")
    item_name = (By.CSS_SELECTOR, ".cart_item_label a")
    item_desc = (By.CSS_SELECTOR, ".inventory_item_desc")
    item_price = (By.CSS_SELECTOR, ".inventory_item_price")
    item_total = (By.CSS_SELECTOR, ".summary_subtotal_label")
    tax_amount = (By.CSS_SELECTOR, ".summary_tax_label")
    finish_button = (By.CSS_SELECTOR, "button#finish")

    def __init__(self, driver):
        self.driver = driver

    def get_checkout_items_list(self):
        return self.driver.find_elements(*self.checkout_items_list)

    def get_checkout_items_details(self):
        items_list = []
        for item in self.get_checkout_items_list():
            name = item.find_element(*self.item_name).text
            desc = item.find_element(*self.item_desc).text
            price = item.find_element(*self.item_price).text.replace("$", "")
            item_detail = {
                "item_name": name,
                "item_desc": desc,
                "item_price": float(price),
            }
            items_list.append(item_detail)
        return items_list

    def calculate_item_total(self, selected_items):
        total = 0
        for item in selected_items:
            total += item["item_price"]
        return total

    def get_item_total(self):
        return float(self.driver.find_element(*self.item_total).text.split("$")[1])

    def get_tax_amount(self):
        return float(self.driver.find_element(*self.tax_amount).text.split("$")[1])

    def get_total(self):
        return self.get_tax_amount() + self.get_item_total()

    def click_finish_button(self):
        self.driver.find_element(*self.finish_button).click()
        return OrderSuccessPage(self.driver)