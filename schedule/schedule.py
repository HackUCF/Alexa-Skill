from ics import Calendar
import requests

HACKUCF_URL="https://calendar.google.com/calendar/ical/calendar%40hackucf.org/public/basic.ics"

def get_next_event():
    # Get the calendar
    c = Calendar(requests.get(HACKUCF_URL).text)

    # Parse out the next event
    return list(c.timeline)[-1].begin

    # return list(c.timeline)

def get_next_meeting():
    return ""

def get_next_workshop():
    return ""

def get_next_ops_meeting():
    return ""

def get_next_competition():
    return ""

if __name__ == "__main__":
    print(get_next_event())
