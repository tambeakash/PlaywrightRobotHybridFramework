import sys
import os

# Add the parent directory to the path so we can import core and pages modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# Global variable to store the browser manager instance
_browser_manager = None


def open_application(url):
    global _browser_manager
    _browser_manager = BrowserManager()
    page = _browser_manager.start_browser()
    page.goto(url)


def login_to_application(username, password):
    # Get the current page from browser manager
    page = _browser_manager.page
    login = LoginPage(page)
    login.login(username, password)


def add_item_and_checkout():
    page = _browser_manager.page
    inventory = InventoryPage(page)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    checkout = CheckoutPage(page)
    checkout.checkout("Akash", "Tambe", "411001")


def close_application():
    _browser_manager.close_browser()