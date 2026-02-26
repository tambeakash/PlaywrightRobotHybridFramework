import os
from playwright.sync_api import sync_playwright

class BrowserManager:

    def __init__(self, headless: bool | None = None):
        # if headless is explicitly passed, use it; otherwise read from env or default to False
        if headless is not None:
            self.headless = headless
        else:
            # check environment variable; CI systems usually set CI=true
            self.headless = os.getenv("HEADLESS", "true" if os.getenv("CI") else "false").lower() in ("1", "true", "yes")

    def start_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.page = self.browser.new_page()
        return self.page

    def close_browser(self):
        self.browser.close()
        self.playwright.stop()