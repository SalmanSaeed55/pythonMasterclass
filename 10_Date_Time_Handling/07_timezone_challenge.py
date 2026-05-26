from datetime import datetime as dt, timezone
import zoneinfo

zones = (
    "Europe/Paris",
    "Europe/London",
    "Asia/Hong_Kong",
    "Africa/Nairobi",
)

utc_now = dt.now(timezone.utc)
for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    required_time = utc_now.astimezone(tz)
    city = zone.split("/")[-1]
    print(f"{city}: {required_time:%Y-%m-%d %H:%M}")