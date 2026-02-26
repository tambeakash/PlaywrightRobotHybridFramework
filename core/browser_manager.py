from playwright.sync_api import sync_playwright

class BrowserManager:

    def start_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        return self.page

    def close_browser(self):
        self.browser.close()
        self.playwright.stop()