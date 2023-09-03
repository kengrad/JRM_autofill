from playwright.sync_api import Page
from settings import email, watcher_password
from locators.locators import AuthWatcherLocators


# авторизация в Watcher

class AuthWatcher():
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def auth_watcher(self):
        self.page.goto(AuthWatcherLocators.link)
        self.page.get_by_placeholder(AuthWatcherLocators.EMAIL).fill(email)
        self.page.get_by_text(AuthWatcherLocators.LOGIN_BUTTON).click()
        self.page.get_by_placeholder(AuthWatcherLocators.PASSWORD).fill(watcher_password)
        self.page.get_by_text(AuthWatcherLocators.LOGIN_BUTTON).click()
