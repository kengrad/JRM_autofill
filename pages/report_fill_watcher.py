from playwright.sync_api import Page
from settings import *


#авторизация в Watcher
def report_fill_watcher(page: Page):
    page.get_by_text('Свернуть').click()
    page.locator('div.day.day--today.day--selected.week__days-sector__day > div.day-body > a').click()
    page.locator('div.day.day--today.day--selected.week__days-sector__day').get_by_text(f'{project}').click()
    page.locator('.content-editable__textarea.selectable').fill(report_watcher)
