import datetime
from zoneinfo import ZoneInfo  # Available in Python 3.9+

def ordinal(n):
    """Convert an integer into its ordinal representation (e.g., 7 -> 7th)."""
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return str(n) + suffix

# Get current time in UK local time (Europe/London)
now = datetime.datetime.now(ZoneInfo("Europe/London"))
month = now.strftime("%B")   # Full month name, e.g., "February"
day = ordinal(now.day)         # Day of month with ordinal, e.g., "7th"
year = now.year                # Year, e.g., 2025

current_date = f"{month} {day}, {year}"
# For example, current_date might be "February 7th, 2025"
