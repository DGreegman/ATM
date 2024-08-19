from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
print(now)
print(day)
print(month)
timestamp = now.timestamp()
print(timestamp)