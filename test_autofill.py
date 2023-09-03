from pages.auth_JRM import *
from pages.auth_watcher import auth_watcher
from pages.report_fill_JRM import *
from pages.report_fill_watcher import report_fill_watcher


def test_jrm_autofill(page):
    auth(page)

    auth_in_report_form(page)
    if date_start:
        date_change(page)
    all_selects(page)
    coment_fill(page)
    issue_and_risks_fill(page)
    submit(page)
    page.wait_for_timeout(JRM_TIMEOUT)  # чтоб полюбоваться на свой отчет и заапрувить


def test_watcher_autofill(page):
    auth_watcher(page)
    report_fill_watcher(page)

    page.wait_for_timeout(WATCHER_TIMEOUT)  # чтоб полюбоваться на свой отчет и заапрувить
