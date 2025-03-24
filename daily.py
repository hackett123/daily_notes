from datetime import date
import os
import calendar

DAILY_ROOT = os.path.join(os.path.expanduser("~"), "daily")
FILETYPE = "md"

today = date.today()
year, month, day = str(today.year), calendar.month_name[today.month], str(today.day)

# Create path to daily note
daily_path = os.path.join(DAILY_ROOT, year, month)
os.makedirs(daily_path, exist_ok=True)


# If daily note doesn't exist yet, create it with the date header
daily_file_path = f"{os.path.join(daily_path, day)}.{FILETYPE}"
if not os.path.exists(daily_file_path):
    with open(daily_file_path, 'w') as daily_file:
        date_header = ' '.join([month, day, year])
        daily_file.write(f"## {date_header}")

# Crucially, this print is fed into the main script - nothing else should print!
print(daily_file_path)
