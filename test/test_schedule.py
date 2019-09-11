from schedule import schedule
from datetime import datetime

def test_get_latest_event():
    """
    get_latest_event() should return a python dict containing the following
    information, so we are going to check typing

    {
        'name': 'General Meeting'
        'date': '2019-11-01T00:00:00+00:00' (python date to string)
    }
    """
    result = schedule.get_latest_event()

    assert result['name'], 'Result has no `name` key'
    assert result['date'], 'Result has not `date` key'

    assert isinstance(result['name'], str), 'name is not a string'
    assert isinstance(result['date'], datetime.date), 'date is not a date'