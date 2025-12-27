import requests
from selenium.webdriver.common.by import By
from utils.base_class import BaseClass

class ProductPage(BaseClass):

    item_details_container = (By.CSS_SELECTOR, ".inventory_details_container")
    item_image = (By.CSS_SELECTOR, ".inventory_details_img")
    item_name = (By.CSS_SELECTOR, ".inventory_details_name")
    item_desc = (By.CSS_SELECTOR, ".inventory_details_desc")
    item_price = (By.CSS_SELECTOR, ".inventory_details_price")

    def __init__(self, driver):
        self.driver = driver

    def get_item_container(self):
        return self.wait_for_element_visibility(self.item_details_container)

    def get_item_details(self):
        product_container = self.get_item_container()
        item_name = product_container.find_element(*self.item_name).text
        item_desc = product_container.find_element(*self.item_desc).text
        item_image = product_container.find_element(*self.item_image).get_attribute("src")
        item_price = product_container.find_element(*self.item_price).text.replace("$", "")
        item_details = {
            "item_name": item_name,
            "item_desc": item_desc,
            "item_image": item_image,
            "item_price": float(item_price)
        }
        return item_details

    def verify_image_not_broken(self):
        product_container = self.get_item_container()
        item_image = product_container.find_element(*self.item_image).get_attribute("src")

        response = requests.head(item_image)
        assert response.status_code == 200, f"Image is broken: {item_image}"



