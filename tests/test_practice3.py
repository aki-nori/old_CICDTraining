import pytest
from playwright.sync_api import Page, expect

from pages import confirm, reserve


class TestReserve(object):
    @pytest.mark.parametrize(
        "date_from,term,breakfast,early,sightseeing,total",
        [
            ("2024/07/01", 3, True, False, False, "24,000円"),
            ("2024/07/02", 2, False, True, False, "15,000円"),
            ("2024/07/03", 1, False, False, True, "8,000円"),
        ],
        ids=["3d-breakfast", "2d-early", "1d-sightseeing"],
    )
    def test_reserve(
        self,
        page: Page,
        date_from: str,
        term: int,
        breakfast: bool,
        early: bool,
        sightseeing: bool,
        total: int,
    ) -> None:
        """宿泊金額が正しいことを確認するテスト"""
        page_reserve = reserve.PageReserve(page)
        page_reserve.navigate()

        # 宿泊内容の設定
        page_reserve.set_date_and_term(date_from, term)
        page_reserve.set_headcount(1)
        page_reserve.select_plan(breakfast, early, sightseeing)
        page_reserve.input_name("てすと太郎")
        page_reserve.select_contact("no")

        # 予約内容の確認
        page_reserve.confirm()

        # 期待値確認
        page_confirm = confirm.PageConfirm(page)
        expect(page_confirm.total_bill).to_have_text(f"合計 {total}（税込み）", timeout=10000)

        # 期待値確認(別解)
        assert page_confirm.get_total_bill() == f"合計 {total}（税込み）"
