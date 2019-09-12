import json

def plaintext_response(text, end_session=False):
    """Prepare a response for Alexa
    
    Arguments:
        text {string} -- Text you want Alexa to say
    
    Keyword Arguments:
        end_session {bool} -- whether or not the shouldEndSession flag is set (default: {False})
    
    Returns:
        string -- JSON ready to return to Alexa
    """
    template = {
        "body": {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": str(text)
                },
                "shouldEndSession": end_session,
                "type": "_DEFAULT_RESPONSE"
            },
            "sessionAttributes": {}
        }
    }
    return json.dumps(template)