class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def checkout(self, first, last, postal):
        self.page.click("text=Checkout")
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", postal)
        self.page.click("#continue")
        self.page.click("#finish")