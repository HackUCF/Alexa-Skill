from ics import Calendar
from datetime import datetime, timezone

import requests

HACKUCF_URL="https://calendar.google.com/calendar/ical/calendar%40hackucf.org/public/basic.ics"

def get_next_event():
    # Get the calendar
    c = Calendar(requests.get(HACKUCF_URL).text)

    # Parse out the next event
    event = filter_events_by(c.timeline)

    if event:
        return {
            'name': event.name,
            'date': event.begin
        }
    else:
        return None

def get_next_meeting():
    # Get the calendar
    c = Calendar(requests.get(HACKUCF_URL).text)

    event = filter_events_by(c.timeline, name='MEETING')
    
    if event:
        return {
            'name': event.name,
            'date': event.begin
        }
    else:
        return None

def get_next_workshop():
    # Get the calendar
    c = Calendar(requests.get(HACKUCF_URL).text)

    event = filter_events_by(c.timeline, name='WORKSHOP')

    if event:
        return {
            'name': event.name,
            'date': event.begin
        }
    else:
        return None

def get_next_ops_meeting():
    # Get the calendar
    c = Calendar(requests.get(HACKUCF_URL).text)

    event = filter_events_by(c.timeline, name='OPS')

    if event:
        return {
            'name': event.name,
            'date': event.begin
        }
    else:
        return None

def get_next_competition():
    # Get the calendar
    c = Calendar(requests.get(HACKUCF_URL).text)

    event = filter_events_by(c.timeline, name='COMPETITION')

    if event:
        return {
            'name': event.name,
            'date': event.begin
        }
    else:
        return None

def filter_events_by(timeline, name=''):
    for item in list(timeline):
        beginning = item.begin

        # [ bit is there so we can tell if it's a marked event
        if datetime.now(timezone.utc) < beginning and f'[{name}' in item.name:
            return item
    return None

if __name__ == "__main__":
    print(get_next_event())
