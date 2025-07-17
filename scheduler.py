from twilio_func import send_rem  # Assuming this is your custom function
from datetime import datetime, date
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import gspread
from google.oauth2.service_account import Credentials
from dateutil.parser import parse

# Google Sheets API scope
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Format today's date
dt = date.today().strftime('%d/%m/%Y')
now_date = datetime.strptime(dt, '%d/%m/%Y')
rem_day = now_date.day
rem_month = now_date.month
rem_year = now_date.year

# Reminder time (14:40) for today in Malawi
t = datetime(rem_year, rem_month, rem_day, 14, 40)

# Use Malawi timezone (CAT)
local = pytz.timezone("Africa/Blantyre")
local_dt = local.localize(t, is_dst=None)

# Convert to UTC for scheduler
utc_dt = local_dt.astimezone(pytz.utc)

# Initialize scheduler
scheduler = BlockingScheduler()

# Google Sheets credentials
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Open worksheet
worksheet = client.open("Reminders").sheet1
list_of_lists = worksheet.get_all_values()

print("📋 Sheet Data:")
print(list_of_lists)

# Schedule reminders
for row in list_of_lists:
    try:
        reminder_date = parse(row[0])
        formatted_date = reminder_date.strftime('%d/%m/%Y')

        if formatted_date == dt:
            # Schedule the reminder
            scheduler.add_job(send_rem, 'date', run_date=utc_dt, args=[row[0], row[1]])
            print(f"✅ Reminder scheduled for {row[0]} - Message: {row[1]}")
        else:
            print(f"⏭️ Skipping: {row[0]}")
    except Exception as e:
        print(f"⚠️ Error processing row {row}: {e}")

# Start the scheduler
print("🕒 Starting scheduler...")
scheduler.start()
