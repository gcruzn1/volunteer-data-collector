
import pytest
import os
import sys

from dotenv import load_dotenv

try:
    from app.main import send_twilio_message, create_service_account_creds
except ImportError:
    # TODO: Determine why __init__.py isn't importing py files from app
    # when running this directly (aka, not in pytest), add root of proj to python path
    sys.path.append(os.path.abspath(os.getcwd()))
    from app.main import send_twilio_message, create_service_account_creds


print(os.getcwd())
MASTER_ALERT_NUM = os.getenv("MASTER_ALERT_NUM")

def test_create_service_acct_creds():
    auth = create_service_account_creds()
    assert auth is not None
    print("ok")


def test_messaging():
    current_form_link = "" # enter form link to test here
    errors_from_twilio, message_stats = send_twilio_message([{"name": "Test Person", "number": MASTER_ALERT_NUM, "form_link": current_form_link}], None)
    
    # add descriptive error
    if errors_from_twilio is not None:
        for error in errors_from_twilio:
            print(error)
    assert errors_from_twilio is None or len(errors_from_twilio) == 0, "Error sending message"

    assert message_stats is not None

## testing
# test_messaging()
# print('done')
# test_create_service_acct_creds()
