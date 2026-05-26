import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A %d %B, %Y')
print(pretty_start)

duration = datetime.timedelta(days=15, hours=48)
end = start + duration
print(end)

