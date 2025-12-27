import pytest
import allure
from pages.login_page import LoginPage
from utils.base_class import BaseClass

@pytest.mark.usefixtures("init_browser")
@allure.feature("Sorting Inventory")
class TestSorting(BaseClass):
    logger = BaseClass.get_logger()
    data = BaseClass.get_data_from_json("data.json")

    # Login Credentials
    username = data["login_credentials"]["username"]
    password = data["login_credentials"]["password"]

    @allure.story("Sort by Name (A-Z)")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify product sorting by Name (A-Z) sorts the products in ascending order.")
    def test_a_to_z_name_sort(self):
        self.logger.info("Starting TC-006: Verify product sorting by Name (A-Z) sorts the products in ascending order.")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        self.logger.info("Sort the products by name (A-Z)")
        inventory_page.sort_items(inventory_page.sort_by_az)

        items_name = [name.text for name in inventory_page.get_items_name_list()]

        self.logger.info("Verifying the items are sorted by name (A-Z)")
        assert items_name == sorted(items_name), "Items are not sorted by name"

    @allure.story("Sort by Name (Z-A)")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify product sorting by Name (Z-A) sorts the products in descending alphabetical order.")
    def test_z_to_a_name_sort(self):
        self.logger.info("Starting TC-007: Verify product sorting by Name (Z-A) sorts the products in descending alphabetical order.")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        self.logger.info("Sort the products by name (Z-A)")
        inventory_page.sort_items(inventory_page.sort_by_za)

        items_name = [name.text for name in inventory_page.get_items_name_list()]

        self.logger.info("Verifying the items are sorted by name (Z-A)")
        assert items_name == sorted(items_name, reverse=True), "Items are not sorted by name"

    @allure.story("Sort by Price (Low to High)")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify product sorting by Price (Low to High).")
    def test_low_to_high_sort_price(self):
        self.logger.info("Starting TC-008: Verify product sorting by Price (Low to High).")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        self.logger.info("Sort the products by price low to high")
        inventory_page.sort_items(inventory_page.sort_by_low_high)

        items_price = [float(name.text.replace("$", "")) for name in inventory_page.get_items_price_list()]

        self.logger.info("Verifying the items are sorted by price low to high")
        assert items_price == sorted(items_price), "Items are not sorted by price (Low to High)"

    @allure.story("Sort by Price (High to Low)")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify product sorting by Price (High to Low).")
    def test_high_to_low_sort_price(self):
        self.logger.info("Starting TC-009: Verify product sorting by Price (High to Low).")

        # Initialize page objects
        login_page = LoginPage(self.driver)

        self.logger.info(f"Logging in with username {self.username} and password {self.password}.")
        inventory_page = login_page.login(self.username, self.password)

        self.logger.info("Verifying inventory page loaded")
        inventory_page.verify_inventory_page_loaded()

        self.logger.info("Sort the products by price high to low")
        inventory_page.sort_items(inventory_page.sort_by_high_low)

        items_price = [float(name.text.replace("$", "")) for name in inventory_page.get_items_price_list()]

        self.logger.info("Verifying the items are sorted by price high to low")
        assert items_price == sorted(items_price, reverse=True), "Items are not sorted by price (High to Low)"









