from playwright.sync_api import Page
from settings import login, password
from locators.locators import JrmAuthLocators


# первичная авторизация в JRM
class AuthJrm(Page):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def auth(self):
        self.page.goto(JrmAuthLocators.link)
        self.page.get_by_text('login', exact=True).click()
        self.page.locator(JrmAuthLocators.USERNAME).fill(login)
        self.page.locator(JrmAuthLocators.PASSWORD).fill(password)
        self.page.locator(JrmAuthLocators.INPUT_BUTTON).click()
