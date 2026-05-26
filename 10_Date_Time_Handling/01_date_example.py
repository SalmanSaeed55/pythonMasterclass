import datetime
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A %d %B, %Y')
print(pretty_start)

year = start.year
month = start.month
day = start.day
print(f"Month: {month}, Day: {day}, year: {year}")

today = datetime.date.today()
print(today)
print(today.strftime("%A"))
print(today.weekday())