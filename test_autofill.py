from pages.auth import *
from pages.report_fill import *

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
    page.wait_for_timeout(5000)
