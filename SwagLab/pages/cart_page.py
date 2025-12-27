import random
from selenium.webdriver.common.by import By
from pages.checkout_page_one import CheckoutPageOne

class CartPage:

    cart_items_list = (By.CSS_SELECTOR, ".cart_list .cart_item")
    item_name = (By.CSS_SELECTOR, ".cart_item_label a")
    item_desc = (By.CSS_SELECTOR, ".inventory_item_desc")
    item_price = (By.CSS_SELECTOR, ".inventory_item_price")
    remove_buttons = (By.XPATH, "//button[normalize-space()='Remove']")
    continue_shopping_button = (By.CSS_SELECTOR, "button#continue-shopping")
    checkout_button = (By.CSS_SELECTOR, "button.checkout_button")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items_list(self):
        return self.driver.find_elements(*self.cart_items_list)

    def get_cart_items_details(self):
        items_list = []
        for item in self.get_cart_items_list():
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

    def remove_item_from_cart(self, remove_count, cart_items_list):
        for _ in range(int(remove_count)):
            remove_buttons = self.driver.find_elements(*self.remove_buttons)
            item_names_list = self.driver.find_elements(*self.item_name)

            item_to_remove = random.choice(cart_items_list)
            item_name = item_to_remove["item_name"]

            for index, item in enumerate(item_names_list):
                if item_name == item.text:
                    remove_buttons[index].click()
                    break

            # remove from your stored list
            cart_items_list = [
                item for item in cart_items_list
                if item["item_name"] != item_name
            ]

        return cart_items_list

    def click_continue_shopping_button(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPageOne(self.driver)














