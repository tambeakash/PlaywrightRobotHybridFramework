import sys
import os
import time
from datetime import datetime

# Add the parent directory to the path so we can import core and pages modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from robot.api import logger

# Global variable to store the browser manager instance
_browser_manager = None
def _save_and_attach_screenshot(name: str) -> None:
    """Save a screenshot to `allure-results/` and attach if Allure is available.

    Falls back to embedding the image into Robot log if Allure is not present.
    """
    try:
        if not _browser_manager:
            return
        page = _browser_manager.page
        os.makedirs("allure-results", exist_ok=True)
        timestamp = int(time.time() * 1000)
        filename = f"{name}_{timestamp}.png"
        path = os.path.join("allure-results", filename)
        page.screenshot(path=path)

        # Try to attach to Allure results (if dependency is installed and listener used)
        try:
            import allure
            from allure_commons.types import AttachmentType

            try:
                # Use allure.attach.file when available
                allure.attach.file(path, name=name, attachment_type=AttachmentType.PNG)
            except Exception:
                # Older versions or different API
                with open(path, "rb") as f:
                    allure.attach(f.read(), name=name, attachment_type=AttachmentType.PNG)
        except Exception:
            # Fallback: embed into Robot log so it's visible in Robot reports
            logger.info(f'<img src="{path}">', html=True)
    except Exception as e:
        logger.warn(f"Failed to capture screenshot: {e}")


def open_application(url):
    global _browser_manager
    try:
        _browser_manager = BrowserManager()
        page = _browser_manager.start_browser()
        page.goto(url)
    except Exception as e:
        _save_and_attach_screenshot("open_application_error")
        raise


def login_to_application(username, password):
    try:
        # Get the current page from browser manager
        page = _browser_manager.page
        login = LoginPage(page)
        login.login(username, password)
    except Exception as e:
        _save_and_attach_screenshot("login_to_application_error")
        raise


def add_item_and_checkout():
    try:
        page = _browser_manager.page
        inventory = InventoryPage(page)
        inventory.add_product_to_cart()
        inventory.go_to_cart()

        checkout = CheckoutPage(page)
        checkout.checkout("Akash", "Tambe", "411001")
    except Exception as e:
        _save_and_attach_screenshot("add_item_and_checkout_error")
        raise


def close_application():
    try:
        if _browser_manager:
            _browser_manager.close_browser()
    except Exception:
        _save_and_attach_screenshot("close_application_error")
        raise


def read_users_from_csv(path: str):
    """Read a CSV file of users and return a list of dicts.

    Each row must contain headers: username,password,first,last,postal
    """
    import csv

    users = []
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(row)
    except Exception as e:
        logger.warn(f"Failed to read users from CSV '{path}': {e}")
        raise
    return users