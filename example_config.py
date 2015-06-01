import os

DEBUG = True

curdir = os.path.abspath(os.path.dirname(__file__))

QUESTIONNAIRE_DIR = os.path.join(curdir, 'questionnaires')
QUESTIONNAIRE_SUBMISSIONS_DIR = os.path.join(curdir, 'submissions')

QUESTIONNAIRE_BASIC_AUTH = ('admin', 'secret')

QUESTIONNAIRE_DEFAULTS = {
    "submit": "Submit",
    "messages": {
        "error": {
            "required": "Field is required",
            "invalid": "Invalid value"
        },
        "success": "Thank you! Your form has been submitted!"
    }
}

