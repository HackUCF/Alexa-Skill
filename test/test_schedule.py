from schedule import schedule
from datetime import datetime

def test_get_next_event():
    """
    get_next_meeting() should return a python dict containing the following
    information, so we are going to check typing.

    {
        'name': 'General Meeting'
        'date': '2019-11-01T00:00:00+00:00' (python date to string)
    }
    """
    result = schedule.get_next_event()

    assert result['name'], 'Result has no `name` key'
    assert result['date'], 'Result has not `date` key'

    assert isinstance(result['name'], str), 'name is not a string'
    assert isinstance(result['date'], datetime.date), 'date is not a date'

def test_get_next_meeting():
    """
    get_next_meeting() should return a python dict containing the following
    information, so we are going to check typing.

    {
        'name': 'General Meeting'
        'date': '2019-11-01T00:00:00+00:00' (python date to string)
    }
    """
    result = schedule.get_next_meeting()

    assert result['name'], 'Result has no `name` key'
    assert result['date'], 'Result has not `date` key'

    assert isinstance(result['name'], str), 'name is not a string'
    assert isinstance(result['date'], datetime.date), 'date is not a date'

def test_get_next_workshop():
    """
    get_next_workshop() should return a python dict containing the following
    information, so we are going to check typing.

    {
        'name': 'Red Team Workshop'
        'date': '2019-11-01T00:00:00+00:00' (python date to string)
    }
    """
    result = schedule.get_next_workshop()

    assert result['name'], 'Result has no `name` key'
    assert result['date'], 'Result has not `date` key'

    assert isinstance(result['name'], str), 'name is not a string'
    assert isinstance(result['date'], datetime.date), 'date is not a date'

def test_get_next_ops_meeting():
    """
    get_next_ops_meeting() should return a python dict containing the following
    information, so we are going to check typing.

    {
        'name': 'Operations Meeting'
        'date': '2019-11-01T00:00:00+00:00' (python date to string)
    }
    """
    result = schedule.get_next_workshop()

    assert result['name'], 'Result has no `name` key'
    assert result['date'], 'Result has not `date` key'

    assert isinstance(result['name'], str), 'name is not a string'
    assert isinstance(result['date'], datetime.date), 'date is not a date'

def test_get_next_competition():
    """
    get_next_competition() should return a python dict containing the following
    information, so we are going to check typing.

    {
        'name': 'ISTS'
        'date': '2019-11-01T00:00:00+00:00' (python date to string)
    }
    """
    result = schedule.get_next_competition()

    assert result['name'], 'Result has no `name` key'
    assert result['date'], 'Result has not `date` key'

    assert isinstance(result['name'], str), 'name is not a string'
    assert isinstance(result['date'], datetime.date), 'date is not a date'