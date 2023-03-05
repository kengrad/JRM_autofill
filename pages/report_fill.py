from playwright.sync_api import Page

from locators import *
from settings import *


# Ввод логина и пароля на странице отчета
def auth2(page: Page):
    page.locator("#id_login").fill(login)
    page.locator("#id_password").fill(password)


# Выбор всех опций(проект, пользователь, платформа, тестер, группа, заголовок в письме)
def all_selects(page: Page):
    page.select_option("#id_project", value=project)
    page.select_option("#id_username", value=username)
    page.select_option("#id_platform", value=platform)
    page.select_option("#id_tester", value=tester)
    page.select_option("#id_group", value=group)
    page.locator("#id_subject").fill("[{project}] Отчёт по тестированию {date}")


# Изменине периода отчета, если date-start='' - по умолчанию сегодняшняя дата
def date_change(page: Page):
    page.locator('#date-start').click()
    page.locator(f"{parent_selector_start} >> {child_selector_start}").click()
    page.locator('#date-end').click()
    page.locator(f"{parent_selector_end} >> {child_selector_end}").click()


# Заполнения коментария (отчета)
def coment_fill(page: Page):
    page.locator("#id_comment").fill(coment)


# Заполнение проблем и рисокв
def issue_and_risks_fill(page: Page):
    page.locator("#id_issues_and_risks").fill(issue_risks)


# Подтверждение и отправка отчета
def submit(page: Page):
    page.locator("input[type='submit']").click()
    # page.locator("input[type='submit']").click()
