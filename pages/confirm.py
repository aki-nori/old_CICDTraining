from playwright.sync_api import Page


class PageConfirm(object):
    def __init__(self, page: Page):
        self.page = page
        self.total_bill = page.locator("#total-bill")

    def get_total_bill(self) -> str:
        return self.total_bill.inner_text()