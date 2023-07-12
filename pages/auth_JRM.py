from playwright.sync_api import Page
from settings import login, password
from locators.locators import JrmAuthLocators


#первичная авторизация в JRM
def auth(page: Page):
    page.goto(JrmAuthLocators.link)
    page.get_by_text('login', exact=True).click()
    page.locator(JrmAuthLocators.USERNAME).fill(login)
    page.locator(JrmAuthLocators.PASSWORD).fill(password)
    page.locator(JrmAuthLocators.INPUT_BUTTON).click()