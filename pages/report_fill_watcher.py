from handlers import reformat_date, reformat_today_date
from pages.auth_watcher import AuthWatcher
from settings import report_watcher, project, WATCHER_TIMEOUT, date_start
from locators.locators import WatcherLocators


class WatcherFill(AuthWatcher):
    def report_fill_watcher(self):
        self.page.get_by_text('Свернуть').click()
        self.page.locator(WatcherLocators.CHOOSE_DAY).click()
        self.page.locator(WatcherLocators.CHOOSE_PROJECT).get_by_text(f'{project}').click()
        self.page.locator(WatcherLocators.COMMENT).fill(report_watcher)

        self.page.wait_for_timeout(WATCHER_TIMEOUT)  # чтоб полюбоваться на свой отчет и заапрувить
