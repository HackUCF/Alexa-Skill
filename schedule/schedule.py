from ics import Calendar
import requests

HACKUCF_URL="https://calendar.google.com/calendar/ical/calendar%40hackucf.org/public/basic.ics"

def get_latest_event():
    # Get the calendar
    c = Calendar(requests.get(HACKUCF_URL).text)

    # Parse out the next event
    return list(c.timeline)[-1].begin
    # return list(c.timeline)

if __name__ == "__main__":
    print(get_latest_event())
