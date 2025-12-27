import pytest
from utils.BaseClass import BaseClass
from pages.practice_component_page import PracticeComponentPage

@pytest.mark.usefixtures("browser_setup")
class TestDragAndDrop(BaseClass):
    logger = BaseClass.get_logger()

    def test_drag_and_drop_image_to_trash(self):
        # Initializing page objects
        components = PracticeComponentPage(self.driver)

        self.logger.info("Starting TC-001: Verify drag-and-drop of an image to the Trash in the Photo Manager tab.")
        drag_drop_page = components.open_drag_drop_page()

        self.wait_for_page_load("draganddrop", drag_drop_page.main_container)
        self.open_tab(drag_drop_page.photo_manager_tab)

        # ---- Step 1: choose how many images to remove ----
        images_to_move_count = 2

        # ---- Step 2: Dragging and dropping random images to trash ----
        moved_images = drag_drop_page.drag_and_drop_image_to_trash(images_to_move_count)
        self.logger.info(f"Moved images with the following srcs are moved to trash: {moved_images}")

        self.logger.info("Collecting all the images present in the trash")
        trash_image_identifiers = drag_drop_page.get_trash_images_src()

        # ---- Step 3: Verifying correct images moved to trash ----
        self.logger.info("Verifying that the correct images are present in the trash")
        assert moved_images == trash_image_identifiers, "The images in trash do not match the ones moved"

        self.driver.switch_to.default_content()

    def test_drag_and_drop_image_to_gallery(self):
        # Initializing page objects
        components = PracticeComponentPage(self.driver)

        self.logger.info("Starting TC-002: Verify drag-and-drop of an image from Trash back to the Gallery in the Photo Manager tab.")
        drag_drop_page = components.open_drag_drop_page()

        self.wait_for_page_load("draganddrop", drag_drop_page.main_container)
        self.open_tab(drag_drop_page.photo_manager_tab)

        # ---- Step 1: choose how many images to move to trash ----
        images_to_move_count = 2

        # ---- Step 2: Dragging and dropping random images to trash ----
        moved_images = drag_drop_page.drag_and_drop_image_to_trash(images_to_move_count)
        self.logger.info(f"Moved images with the following srcs are moved to trash: {moved_images}")

        self.logger.info("Collecting all the images present in the trash")
        trash_image_identifiers = drag_drop_page.get_trash_images_src()

        # ---- Step 3: Verifying correct images moved to trash ----
        self.logger.info("Verifying that the correct images are present in the trash")
        assert moved_images == trash_image_identifiers, "The images in trash do not match the ones moved"

        # ---- Step 4: choose how many images to add back to gallery ----
        self.logger.info(f"Moving {images_to_move_count} images back to the gallery from trash")
        images_moved_back_to_gallery = drag_drop_page.drag_and_drop_image_to_gallery(images_to_move_count)

        # ---- Step 5: Dragging and dropping random images to gallery ----
        self.logger.info("Collecting all the images present in the gallery")
        gallery_images = drag_drop_page.get_gallery_images_src()

        # ---- Step 6: Verifying correct images moved to gallery ----
        self.logger.info("Verifying that the correct images are present in the gallery")
        for img_src in images_moved_back_to_gallery:
            assert img_src in gallery_images, f"Image {img_src} not found in gallery after moving back"

        self.driver.switch_to.default_content()






