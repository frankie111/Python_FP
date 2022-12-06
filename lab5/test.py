from datetime import datetime, timedelta

current_date = datetime.now()
print(f"Current date: {current_date}" )

current_date += timedelta(minutes=30)
iso = current_date.isoformat()
date30 = datetime.fromisoformat(iso)
print(f"Current date + 30 min: {date30}" )
