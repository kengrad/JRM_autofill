from datetime import datetime


def reformat_today_date():
    today_date = str(datetime.today())
    return f"{datetime.strptime(today_date[:10], '%Y-%m-%d').strftime('%d.%m')}"


