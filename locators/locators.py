class JrmAuthLocators:
    link = "http://10.39.3.226:8000/form/"
    USERNAME = "#id_username"
    PASSWORD = "#id_password"
    INPUT_BUTTON = "input[type='submit']"


class JrmLocators:
    LOGIN = "#id_login"
    PASSWORD = "#id_password"

    PROJECT = "#id_project"
    USERNAME = "#id_username"
    PLATFORM = "#id_platform"
    TESTER = "#id_tester"
    GROUP = "#id_group"
    SUBJECT = "#id_subject"

    DATE_START = '#date-start'
    DATE_END = '#date-end'

    COMMENT = "#id_comment"
    ISSUES_AND_RISKS = "#id_issues_and_risks"
    SUBMIT_BUTTON = "input[type='submit']"


class AuthWatcherLocators:
    link = "https://watcher.kode.ru/signin"
    EMAIL = "Email для кодеров"
    LOGIN_BUTTON = 'Войти'
    PASSWORD = "Введите пароль"


class WatcherLocators:
    CHOOSE_DAY = '.flat-button.flat-button--with-icon.flat-button--theme-red-bright.flat-button--highlighted'
    CHOOSE_PROJECT = '.items-list.search-list__list'
    COMMENT = '.content-editable__textarea.selectable'
