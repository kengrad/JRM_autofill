from pytest import mark

from pages.auth_JRM import *
from pages.report_fill_JRM import JrmFill
from pages.report_fill_watcher import WatcherFill
from settings import date_start


class TestAutofill:
    def test_jrm_autofill(self, page: Page) -> None:
        page = JrmFill(page)
        page.auth()
        page.auth_in_report_form()
        if date_start:
            page.date_change()
        page.all_selects()
        page.coment_fill()
        page.issue_and_risks_fill()
        page.submit()

    @mark.debug
    def test_watcher_autofill(self, page: Page) -> None:
        page = WatcherFill(page)
        page.auth_watcher()
        page.report_fill_watcher()
