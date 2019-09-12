import json

def plaintext_response(text, end_session=False):
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