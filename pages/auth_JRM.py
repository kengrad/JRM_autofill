from playwright.sync_api import Page
from settings import *


#первичная авторизация в JRM
def auth(page: Page):
    page.get_by_text('login', exact=True).click()
    page.locator("#id_username").fill(login)
    page.locator("#id_password").fill(password)
    page.locator("input[type='submit']").click()



