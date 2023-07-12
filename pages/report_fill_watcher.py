from playwright.sync_api import Page
from settings import *
from locators.locators import WatcherLocators


#авторизация в Watcher
def report_fill_watcher(page: Page):
    page.get_by_text('Свернуть').click()
    page.locator(WatcherLocators.CHOOSE_DAY).click()
    page.locator(WatcherLocators.CHOOSE_PROJECT).get_by_text(f'{project}').click()
    page.locator(WatcherLocators.COMMENT).fill(report_watcher)
