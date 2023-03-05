from settings import *


parent_selector_start = "#datepickers-container > div:nth-child(1)"
child_selector_start = f"div[data-date='{date_start}'][data-month='{str(int(month_start)-1)}'][data-year='{year_start}']"

parent_selector_end = "#datepickers-container > div:nth-child(2)"
child_selector_end = f"div[data-date='{date_end}'][data-month='{str(int(month_end)-1)}'][data-year='{year_end}']"