from pages.auth_JRM import AuthJrm
from settings import *
from locators.locators import JrmLocators


class JrmFill(AuthJrm):

    def auth_in_report_form(self):
        self.page.locator(JrmLocators.LOGIN).fill(login)
        self.page.locator(JrmLocators.PASSWORD).fill(password)

    # Выбор всех опций(проект, пользователь, платформа, тестер, группа, заголовок в письме)
    def all_selects(self):
        self.page.select_option(JrmLocators.PROJECT, value=project)
        self.page.select_option(JrmLocators.USERNAME, value=username)
        self.page.select_option(JrmLocators.PLATFORM, value=platform)
        self.page.select_option(JrmLocators.TESTER, value=tester)
        self.page.select_option(JrmLocators.GROUP, value=group)
        self.page.locator(JrmLocators.SUBJECT).fill("[{project}] Отчёт по тестированию {date}")

    # Изменине периода отчета, если date-start='' - по умолчанию сегодняшняя дата
    def date_change(self):
        self.page.locator(JrmLocators.DATE_START).fill(date_start)
        self.page.locator(JrmLocators.DATE_END).fill(date_end)

    # Заполнения коментария (отчета)
    def coment_fill(self):
        self.page.locator(JrmLocators.COMMENT).fill(report_JRM)

    # Заполнение проблем и рисокв
    def issue_and_risks_fill(self):
        self.page.locator(JrmLocators.ISSUES_AND_RISKS).fill(issue_risks)

    # Подтверждение и отправка отчета
    def submit(self):
        self.page.locator(JrmLocators.SUBMIT_BUTTON).click()
        self.page.wait_for_timeout(JRM_TIMEOUT)  # чтоб полюбоваться на свой отчет и заапрувить
