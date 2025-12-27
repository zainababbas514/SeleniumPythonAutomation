from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.BaseClass import BaseClass

class DragDropPage(BaseClass):

    photo_manager_tab = (By.XPATH, "//li[@id='Photo Manager']")
    main_container = (By.CSS_SELECTOR, ".row.page_sidebar")
    gallery_images = (By.CSS_SELECTOR, "#gallery .ui-draggable")
    gallery = (By.CSS_SELECTOR, "#gallery")
    trash = (By.CSS_SELECTOR, "#trash")
    demo_frame = (By.CSS_SELECTOR, ".demo-frame")
    gallery_image_headings = (By.CSS_SELECTOR, "#gallery .ui-widget-header")
    gallery_images_src = (By.CSS_SELECTOR, "#gallery .ui-draggable img")
    trash_images = (By.CSS_SELECTOR, "#trash .ui-draggable img")

    def __init__(self, driver):
        self.driver = driver

    def get_trash_container(self):
        return self.driver.find_element(*self.trash)

    def get_gallery_container(self):
        return self.driver.find_element(*self.gallery)

    def get_gallery_image_heading(self):
        return self.driver.find_elements(*self.gallery_image_headings)

    def get_gallery_images_src(self):
        gallery_images_src = self.driver.find_elements(*self.gallery_images_src)
        return [img.get_attribute('src') for img in gallery_images_src]

    def get_trash_images(self):
        return self.driver.find_elements(*self.trash_images)

    def get_trash_images_src(self):
        trash_images_src = self.driver.find_elements(*self.trash_images)
        return [img.get_attribute('src') for img in trash_images_src]

    def wait_for_image_in_trash(self, image_src, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: image_src in self.get_trash_images_src(),
            message=f"Image with src {image_src} not found in trash after {timeout} seconds"
        )

    def wait_for_image_in_gallery(self, image_src, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: image_src in self.get_gallery_images_src(),
            message=f"Image with src {image_src} not found in trash after {timeout} seconds"
        )

    def drag_and_drop_image_to_trash(self, count_of_items_move_to_trash):
        actions = ActionChains(self.driver)

        self.switch_to_frame(self.demo_frame)
        self.wait_for_element_visibility(self.gallery)
        self.wait_for_element_visibility(self.trash)

        # Get all gallery images
        gallery_images = self.driver.find_elements(*self.gallery_images)

        # Get gallery images src
        gallery_images_src = self.get_gallery_images_src()

        # Trash container
        trash = self.get_trash_container()

        selected_image_identifiers = []

        for _ in range(count_of_items_move_to_trash):
            # pick a random image from current gallery list
            random_index = self.generate_random_number(len(gallery_images))

            image_element = gallery_images[random_index]
            image_src = gallery_images_src[random_index]

            # drag it
            actions.drag_and_drop(image_element, trash).perform()

            selected_image_identifiers.append(image_src)

            # wait until this src appears in trash
            self.wait_for_image_in_trash(image_src)

            # refresh lists because the gallery DOM changed
            gallery_images = self.driver.find_elements(*self.gallery_images)
            gallery_images_src = self.get_gallery_images_src()

        return selected_image_identifiers

    def drag_and_drop_image_to_gallery(self, count_of_items_move_to_gallery):
        actions = ActionChains(self.driver)

        # Get all trash images
        trash_images = self.driver.find_elements(*self.trash_images)

        # Get all trash images src
        trash_images_src = self.get_trash_images_src()
        selected_image_identifiers = []

        print(len(trash_images))
        for _ in range(count_of_items_move_to_gallery):
            random_index = self.generate_random_number(len(trash_images))
            print(random_index)
            random_image = trash_images[random_index]
            actions.drag_and_drop(random_image, self.get_gallery_container()).perform()
            selected_image_identifiers.append(trash_images_src[random_index])
            self.wait_for_image_in_gallery(trash_images_src[random_index])

            # refresh lists because the gallery DOM changed
            trash_images = self.driver.find_elements(*self.trash_images)
            trash_images_src = self.get_trash_images_src()

        return selected_image_identifiers


















