from playwright.sync_api import Page

from settings import *
from locators.locators import JrmLocators


# Ввод логина и пароля на странице отчета
def auth_in_report_form(page: Page):
    page.locator(JrmLocators.LOGIN).fill(login)
    page.locator(JrmLocators.PASSWORD).fill(password)


# Выбор всех опций(проект, пользователь, платформа, тестер, группа, заголовок в письме)
def all_selects(page: Page):
    page.select_option(JrmLocators.PROJECT, value=project)
    page.select_option(JrmLocators.USERNAME, value=username)
    page.select_option(JrmLocators.PLATFORM, value=platform)
    page.select_option(JrmLocators.TESTER, value=tester)
    page.select_option(JrmLocators.GROUP, value=group)
    page.locator(JrmLocators.SUBJECT).fill("[{project}] Отчёт по тестированию {date}")


# Изменине периода отчета, если date-start='' - по умолчанию сегодняшняя дата
def date_change(page: Page):
    page.locator(JrmLocators.DATE_START).fill(date_start)
    page.locator(JrmLocators.DATE_END).fill(date_end)


# Заполнения коментария (отчета)
def coment_fill(page: Page):
    page.locator(JrmLocators.COMMENT).fill(report_JRM)


# Заполнение проблем и рисокв
def issue_and_risks_fill(page: Page):
    page.locator(JrmLocators.ISSUES_AND_RISKS).fill(issue_risks)


# Подтверждение и отправка отчета
def submit(page: Page):
    page.locator(JrmLocators.SUBMIT_BUTTON).click()
