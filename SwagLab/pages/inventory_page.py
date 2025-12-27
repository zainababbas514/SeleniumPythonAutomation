import random
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from utils.base_class import BaseClass

class InventoryPage(BaseClass):

    inventory_items_list = (By.CSS_SELECTOR, '.inventory_list .inventory_item')
    item_image = (By.CSS_SELECTOR, '.inventory_item_img img')
    item_title = (By.CSS_SELECTOR, '.inventory_item_name')
    item_price = (By.CSS_SELECTOR, '.inventory_item_price')
    item_desc = (By.CSS_SELECTOR, '.inventory_item_desc')
    add_to_cart_btn = (By.CSS_SELECTOR, "button.btn_inventory")
    cart_badge = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    cart = (By.CSS_SELECTOR, "a.shopping_cart_link")
    sort_dropdown = (By.CSS_SELECTOR, "select.product_sort_container")

    # Sort dropdown options
    sort_by_az = "az"
    sort_by_za = "za"
    sort_by_low_high = "lohi"
    sort_by_high_low = "hilo"

    def __init__(self, driver):
        self.driver = driver

    def get_inventory_list(self):
        return self.driver.find_elements(*self.inventory_items_list)

    def verify_inventory_page_loaded(self):
        assert "inventory.html" in self.driver.current_url
        assert len(self.get_inventory_list()) > 0

    def verify_inventory_items(self):
        for item in self.get_inventory_list():

            # Image
            self.wait_for_element_visibility(self.item_image)
            image = item.find_element(*self.item_image)
            assert image.is_displayed(), "Image is not displayed!"

            image_src = image.get_attribute("src")
            assert image_src != "", "Image src is empty!"
            response = requests.get(image_src)
            response.raise_for_status()

            # Item name
            item_name = item.find_element(*self.item_title).text
            assert item_name != "", "Item name is empty!"

            # Add to cart button
            add_to_cart_btn = item.find_element(*self.add_to_cart_btn)
            assert add_to_cart_btn.is_displayed() and add_to_cart_btn.is_enabled(), \
                "Add to cart Button is not enabled or displayed!"

            # Price
            price_element = item.find_element(*self.item_price)
            assert price_element.is_displayed(), "Item price is not displayed"
            item_price = price_element.text
            assert item_price != "", "Item price is empty!"

            price_value = float(item_price.replace("$", ""))
            assert price_value > 0, f"Price should be greater than 0, found: {price_value}"

    def get_items_name_list(self):
        return self.driver.find_elements(*self.item_title)

    def get_items_desc_list(self):
        return self.driver.find_elements(*self.item_desc)

    def get_items_price_list(self):
        return self.driver.find_elements(*self.item_price)

    def get_items_image_list(self):
        return self.driver.find_elements(*self.item_image)

    def add_items_to_cart(self, item_count):
        total_items = len(self.get_inventory_list())
        items_list = self.get_inventory_list()
        random_numbers = random.sample(range(0, total_items), int(item_count))
        cart_items = []
        for random_number in random_numbers:
            items_list[random_number].find_element(*self.add_to_cart_btn).click()
            item_name = self.get_items_name_list()[random_number].text
            item_desc = self.get_items_desc_list()[random_number].text
            item_price = self.get_items_price_list()[random_number].text.replace("$", "")
            item = {
                "item_name": item_name,
                "item_desc": item_desc,
                "item_price": float(item_price),
            }
            cart_items.append(item)
        return cart_items

    def verify_cart_badge_count(self, expected_count):
        badge_count = self.driver.find_element(*self.cart_badge).text
        assert badge_count == expected_count, f"Expected {badge_count}, but got {expected_count}"

    def open_cart_page(self):
        self.driver.find_element(*self.cart).click()
        return CartPage(self.driver)

    def verify_added_items_show_remove(self, added_items):
        items_list = self.get_inventory_list()
        added_items_name = [added_item["item_name"] for added_item in added_items]
        for item in items_list:
           item_name = item.find_element(*self.item_title).text
           button_text = item.find_element(*self.add_to_cart_btn).text
           if item_name in added_items_name:
                assert button_text == "Remove", f"{item_name} does not show Remove button!"
           else:
               assert button_text == "Add to cart", f"'{item_name}' shows 'Remove' button while it was not added!"

    def open_product_page(self):
        items_list = self.get_inventory_list()
        random_index = random.randint(0, len(items_list) - 1)
        item_name = self.get_items_name_list()[random_index]
        item_desc = self.get_items_desc_list()[random_index].text
        item_price = self.get_items_price_list()[random_index].text.replace("$", "")
        item_image = self.get_items_image_list()[random_index].get_attribute("src")
        item_details = {
            "item_name": item_name.text,
            "item_desc": item_desc,
            "item_price": float(item_price),
            "item_image": item_image
        }

        item_name.click()
        return item_details, ProductPage(self.driver)

    def sort_items(self, sort_option):
        sort_dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        sort_dropdown.select_by_value(sort_option)











