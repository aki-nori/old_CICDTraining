from playwright.sync_api import Page


class PageReserve(object):
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        """予約画面を開く"""
        self.page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0")

    def set_date_and_term(self, date: str, term: int) -> None:
        """宿泊日と宿泊数を設定する"""

        date_form = self.page.get_by_label("宿泊日")
        date_form.clear()
        date_form.fill(date)
        date_form.press("Tab")

        self.page.get_by_label("宿泊数").fill(str(term))

    def set_headcount(self, headcount: int) -> None:
        """人数を設定する"""

        self.page.get_by_label("人数").fill(str(headcount))

    def select_plan(self, breakfast: bool, early: bool, sightseeing: bool) -> None:
        """追加プランを選択する"""

        self.page.get_by_label("朝食バイキング").set_checked(breakfast)

        self.page.get_by_label("昼からチェックインプラン").set_checked(early)

        self.page.get_by_label("お得な観光プラン").set_checked(sightseeing)

    def input_name(self, username: str) -> None:
        """氏名を入力する"""

        self.page.get_by_label("氏名").fill(username)

    def select_contact(self, value: str) -> None:
        """確認の連絡方法を選択する"""

        self.page.get_by_label("確認のご連絡").select_option(value)

    def confirm(self) -> None:
        """予約内容を確認する"""

        self.page.locator('[data-test="submit-button"]').click()