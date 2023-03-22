from playwright.sync_api import Page
from settings import *


#авторизация в Watcher
def auth_watcher(page: Page):
    page.get_by_placeholder("Email для кодеров").fill(email)
    page.get_by_text('Войти').click()
    page.get_by_placeholder("Введите пароль").fill(watcher_password)
    page.get_by_text('Войти').click()

