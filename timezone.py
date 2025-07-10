import time
print("Your timezone:", time.tzname[0])
offset_sec = time.timezone if not time.localtime().tm_isdst else time.altzone
offset_hours = -offset_sec // 3600
print("UTC Offset (hours):", offset_hours)
print("Current Date:", time.strftime('%Y-%m-%d'))
print("Current Time:", time.strftime('%I:%M %p'))
print("Daylight Saving Time:", "Yes" if time.localtime().tm_isdst else "No")
while True:
    if input("Type 'end' to exit\n").lower() == 'end':
        break