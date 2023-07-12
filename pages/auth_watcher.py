from playwright.sync_api import Page
from settings import *
from locators.locators import AuthWatcherLocators

#авторизация в Watcher
def auth_watcher(page: Page):
    page.goto(AuthWatcherLocators.link)
    page.get_by_placeholder(AuthWatcherLocators.EMAIL).fill(email)
    page.get_by_text(AuthWatcherLocators.LOGIN_BUTTON).click()
    page.get_by_placeholder(AuthWatcherLocators.PASSWORD).fill(watcher_password)
    page.get_by_text(AuthWatcherLocators.LOGIN_BUTTON).click()

