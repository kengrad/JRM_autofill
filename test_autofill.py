from pages.auth_JRM import *
from pages.auth_watcher import auth_watcher
from pages.report_fill_JRM import *
from pages.report_fill_watcher import report_fill_watcher


def test_jrm_autofill(page):
    page.goto("http://10.39.3.226:8000/form/")
    auth(page)
    auth2(page)
    if date_start:
        date_change(page)
    all_selects(page)
    coment_fill(page)
    issue_and_risks_fill(page)
    submit(page)
    page.wait_for_timeout(15000)


def test_watcher_autofill(page):
    page.goto("https://watcher.kode.ru/signin")
    auth_watcher(page)
    report_fill_watcher(page)


    page.wait_for_timeout(15000)
