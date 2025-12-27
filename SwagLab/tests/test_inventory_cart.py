import time

import allure
import pytest
from pages.login_page import LoginPage
from utils.base_class import BaseClass

@pytest.mark.usefixtures("init_browser")
@allure.feature("Inventory and Cart Functionality")
class TestInventoryCart(BaseClass):
    logger = BaseClass.get_logger()
    data = BaseClass.get_data_from_json("data.json")

    # Login Credentials
    username = data["login_credentials"]["username"]
    password = data["login_credentials"]["password"]

    @allure.story("Inventory Validation")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that all products are displayed correctly on the Inventory page.")
    def test_inventory_items(self):
        self.logger.info("Starting TC-001: Verify that all products are displayed correctly on the Inventory page.")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        self.logger.info("Verifying all products load correctly with image, name, price.")
        inventory_page.verify_inventory_items()

    @pytest.mark.parametrize("item_count", data["TC-002"])
    @allure.story("Add items to the cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that a single and multiple products can be successfully added to the cart.")
    def test_add_items_to_cart(self, item_count):
        self.logger.info("Starting TC-002: Verify that a single and multiple products can be successfully added to the cart.")
        allure.dynamic.title(f"TC-002: Add {item_count["add_to_cart_item_count"]} items to cart")
        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        add_item_to_cart_count = item_count["add_to_cart_item_count"]

        self.logger.info(f"Add {add_item_to_cart_count} items to the cart.")
        selected_items = inventory_page.add_items_to_cart(add_item_to_cart_count)

        self.logger.info("Verify cart badge is showing correct item count")
        inventory_page.verify_cart_badge_count(add_item_to_cart_count)

        self.logger.info("Verifying added items showing Remove button")
        inventory_page.verify_added_items_show_remove(selected_items)

    @allure.story("Cart shows added products")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify cart page displays added products correctly.")
    def test_cart_shows_added_items(self):
        self.logger.info("Starting TC-003: Verify cart page displays added products correctly.")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        add_item_to_cart_count = self.data["TC-005"]["add_to_cart_item_count"]

        self.logger.info(f"Add {add_item_to_cart_count} items to the cart.")
        selected_items = inventory_page.add_items_to_cart(add_item_to_cart_count)

        self.logger.info("Verify cart badge is showing correct item count")
        inventory_page.verify_cart_badge_count(add_item_to_cart_count)

        self.logger.info("Open the cart page")
        cart_page = inventory_page.open_cart_page()

        cart_items = cart_page.get_cart_items_details()

        self.logger.info("Verifying selected items and the cart items are the same.")
        assert selected_items == cart_items, "Selected items and the cart items does not match"

    @allure.story("Remove products from the cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify user can remove a product from the cart page successfully.")
    def test_remove_item_from_cart(self):

        self.logger.info("Starting TC-004: Verify user can remove a product from the cart page successfully.")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        add_item_to_cart_count = self.data["TC-003"]["add_to_cart_item_count"]
        remove_item_count = self.data["TC-003"]["remove_from_cart_item_count"]

        self.logger.info(f"Add {add_item_to_cart_count} items to the cart.")
        selected_items = inventory_page.add_items_to_cart(add_item_to_cart_count)

        self.logger.info("Verify cart badge is showing correct item count")
        inventory_page.verify_cart_badge_count(add_item_to_cart_count)

        self.logger.info("Open the cart page")
        cart_page = inventory_page.open_cart_page()

        cart_items = cart_page.get_cart_items_details()

        self.logger.info("Verifying selected items and the cart items are the same.")
        assert selected_items == cart_items, "Selected items and the cart items does not match"

        remove_item = cart_page.remove_item_from_cart(remove_item_count, cart_items)
        cart_items = cart_page.get_cart_items_details()

        assert remove_item == cart_items, "Selected items and the cart items does not match"

        self.logger.info("Verify cart badge is showing correct item count after removing items from cart")
        inventory_page.verify_cart_badge_count(str(len(remove_item)))

        self.logger.info("Clicking continue shopping button")
        cart_page.click_continue_shopping_button()

        self.logger.info("Verifying correct items show Remove button")
        inventory_page.verify_added_items_show_remove(cart_items)

    @allure.story("Product detail page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that clicking a product opens its details page.")
    def test_item_click_open_product(self):
        self.logger.info("Starting TC-005: Verify that clicking a product opens its details page.")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded.")
        inventory_page.verify_inventory_page_loaded()

        self.logger.info("Clicking on random product to open the product page")
        selected_item_details, product_page = inventory_page.open_product_page()

        self.logger.info("Verifying product image is not broken")
        product_page.verify_image_not_broken()

        self.logger.info("Verifying correct product details are showing")
        assert selected_item_details == product_page.get_item_details(), f"Item mismatch! Expected: {selected_item_details}, Got: {product_page.get_item_details()}"


















