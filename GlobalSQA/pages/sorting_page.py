from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utils.BaseClass import BaseClass

class SortingPage(BaseClass):
    simple_list_tab = (By.XPATH, "//li[@id='Simple List']")
    main_container = (By.CSS_SELECTOR, ".resp-tabs-container")
    iframe = (By.XPATH, "(//iframe[@class='demo-frame'])[3]")
    sortable_container = (By.CSS_SELECTOR, "ul#sortable")
    sortable_list = (By.CSS_SELECTOR, "#sortable li.ui-state-default")

    def __init__(self, driver):
        self.driver = driver

    def get_sortable_list(self):
        sortable_list = self.wait_for_all_element_visibility(self.sortable_list)
        return sortable_list

    def get_reorder_indexes(self, move_item, drop_location):
        items = self.get_sortable_list()
        move_item_index = None

        if drop_location == "TOP":
            drop_location_index = 0
        elif drop_location == "BOTTOM":
            drop_location_index = len(items) - 1
        else:
            drop_location_index = None

        for index, item in enumerate(items):
            print(item.text)
            if item.text == move_item:
                move_item_index = index

            if drop_location_index is None and item.text == drop_location :
                drop_location_index = index

            if move_item_index is not None and drop_location_index is not None:
                break

        return move_item_index, drop_location_index

    def reorder_item(self, move_item, drop_location):

        actions = ActionChains(self.driver)
        elements = self.get_sortable_list()

        element_to_move_index, drop_location_index = self.get_reorder_indexes(move_item, drop_location)
        source = elements[element_to_move_index]
        target = elements[drop_location_index]

        # Start dragging
        actions.click_and_hold(source).perform()

        # Move over the target element
        actions.move_to_element(target).perform()

        # SMALL OFFSET — this is required for sortable widgets to trigger reordering
        # Use negative yoffset to drop before and positive to drop after
        actions.move_by_offset(0, 10).perform()

        # Release the mouse to complete the drop
        actions.release().perform()

    def verify_list_order(self, expected_order):
        # Get current list order from the UI
        original_list_order = [item.text for item in self.get_sortable_list()]

        # Convert "Item1,Item2,Item3" → ["Item1", "Item2", "Item3"]
        expected_order_list = expected_order.split(",")

        assert original_list_order == expected_order_list,  f"Order mismatch.\nExpected: {expected_order_list}\nActual: {original_list_order}"









