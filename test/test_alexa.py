from alexa import response
import json
import pytest

@pytest.mark.parametrize(
    "input_text, end_session",
    [
        ("Test", False),
        ("Test", True),
        ("\n\t", False),
        (1, False),
        (True, False),
        (0.5, False)
    ]
)
def test_build_text_response(input_text, end_session):
    """
    response.text_response(text) should format the text for Alexa so that Alexa
    will read the text to the user in response to their query
    """
    res = response.plaintext_response(input_text, end_session=end_session)

    res_json = json.loads(res)

    assert res_json['body']['response']['outputSpeech']['type'] == 'PlainText'
    assert res_json['body']['response']['outputSpeech']['text'] == str(input_text)
    assert res_json['body']['response']['shouldEndSession'] == end_session

# Test opening text
# "INSERT OPENING TEXT HERE"
def test_opening_text():
    assert 1==0

# Test NextEvent intent
# Gives the user the next general meeting (?) on the Hack@UCF Calendar
def test_next_event_intent():
    assert 1==0

# Test NextMeeting intent
# Gives the user the next general meeting (?) on the Hack@UCF Calendar
def test_next_meeting_intent():
    assert 1==0

# Test NextOps intent
# Gives the user the next general meeting (?) on the Hack@UCF Calendar
def test_next_ops_meeting_intent():
    assert 1==0

# Test NextWorkshop intent
# Gives the user the next general meeting (?) on the Hack@UCF Calendar
def test_next_workshop_intent():
    assert 1==0

# Test AMAZON.HelpIntent intent
# Gives some help on how to use the skill
def test_help_intent():
    assert 1==0

# Test AMAZON.StopIntent
# Sets `shouldEndSession` to true
def test_stop_intent():
    assert 1==0

# Test AMAZON.FallbackIntent
# "I didn't understand that"
def test_fallback_intent():
    assert 1==0