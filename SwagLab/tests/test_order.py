import allure
import pytest
from pages.login_page import LoginPage
from utils.base_class import BaseClass

@pytest.mark.usefixtures("init_browser")
@allure.feature("Order Products")
class TestOrder(BaseClass):
    logger = BaseClass.get_logger()
    data = BaseClass.get_data_from_json("data.json")

    # Login Credentials
    username = data["login_credentials"]["username"]
    password = data["login_credentials"]["password"]

    @allure.story("Test complete order flow")
    @allure.description("Verify user can order items successfully.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_items(self):
        self.logger.info("Starting TC-010: Verify user can order items successfully.")

        # Initialize Login Page
        login_page = LoginPage(self.driver)

        # Test Data
        test_data = self.data["TC-010"]
        first_name = test_data["checkout_form"]["first_name"]
        last_name = test_data["checkout_form"]["last_name"]
        postal_code = test_data["checkout_form"]["postal_code"]
        expected_thank_you_message = test_data["thank_you_message"]
        expected_delivery_message = test_data["delivery_message"]
        add_item_to_cart_count = test_data["add_to_cart_item_count"]

        # Login
        self.logger.info(f"Logging in as '{self.username}'.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying the Inventory page is loaded.")
        inventory_page.verify_inventory_page_loaded()

        # Add Items
        self.logger.info(f"Adding {add_item_to_cart_count} items to cart.")
        selected_items = inventory_page.add_items_to_cart(add_item_to_cart_count)

        self.logger.info("Verifying cart badge count.")
        inventory_page.verify_cart_badge_count(add_item_to_cart_count)

        # Cart Page
        self.logger.info("Opening the cart page.")
        cart_page = inventory_page.open_cart_page()
        cart_items = cart_page.get_cart_items_details()

        self.logger.info("Verifying cart items match selected items.")
        assert selected_items == cart_items, "Selected items and the items in the cart do not match."

        # Checkout Step 1
        self.logger.info("Clicking Checkout button.")
        checkout_page_one = cart_page.click_checkout_button()

        self.logger.info("Filling checkout form.")
        checkout_page_one.fill_checkout_form(first_name, last_name, postal_code)

        # Checkout Step 2
        self.logger.info("Clicking Continue button.")
        checkout_page_two = checkout_page_one.click_continue_button()
        checkout_items = checkout_page_two.get_checkout_items_details()

        self.logger.info("Verifying checkout items match selected items.")
        assert checkout_items == selected_items, "Selected items and the items on the checkout page do not match."

        # Verify Totals
        expected_total = checkout_page_two.calculate_item_total(selected_items)
        actual_total = checkout_page_two.get_item_total()

        self.logger.info("Verifying item total matches expected total.")
        assert expected_total == actual_total, f"Expected total {expected_total}, but got {actual_total}."

        # Finish Order
        order_success_page = checkout_page_two.click_finish_button()

        self.logger.info("Verifying Thank You message.")
        actual_thank_you_message = order_success_page.get_thank_you_message()
        assert actual_thank_you_message == expected_thank_you_message, "Thank You message does not match."

        self.logger.info("Verifying delivery message.")
        actual_delivery_message = order_success_page.get_order_delivery_message()
        assert actual_delivery_message == expected_delivery_message, "Delivery message does not match."

        # Back to Inventory
        self.logger.info("Clicking Back Home button.")
        order_success_page.click_back_home_button()

        self.logger.info("Verifying redirection to Inventory page.")
        inventory_page.verify_inventory_page_loaded()