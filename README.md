# q10r

q10r is a simple questionnaire web app. It produces questionnaires
from JSON files and stores submissions in JSON files under different
directory. q10r also provides a page for viewing questionnaire
results.

## Demo

http://vlevit.org/q10r/ <-- list of questionnaires  
http://vlevit.org/q10r/texteditor <-- questionnaire "texteditor"  
http://vlevit.org/q10r/texteditor/results <-- results for
questionnaire "texteditor"

## Installation

q10r is a Flask blueprint. To install dependencies run

    pip install -r requirements.txt

Then create a new application (or embed to the existing one). See
`example_app.py` as for example. Create config similar to
`example_config.py`. It must contain `QUESTIONNAIRE_DIR` which must
point to a directory with questionnaire files and
`QUESTIONNAIRE_SUBMISSIONS_DIR` where submissions will be written.

## Usage

Site root provides a list of existing questionnaires with links to
forms and results.

Look at `questionnaires/texteditor.json` for a questionnaire example.
Each questionnaire is a dict which may contain the following fields:

    extends
    title
    comment
    template
    submit
    questions

With `extends` you can specify a different json file as a base, it
should be prefixed with `_` so it will not be considered a stand-alone
questionnaire. With `template` you can specify alternative template.
If not specified `questionnaire.html` is used. `questions` is a list
of objects which represent (surprisingly) questions. Each such object
must be one of the following types: `string` (text), `text`
(textarea), `radio` and `checkbox`. `radio`, `checkbox` questions must
have `options`. To mark option as "other" field (a field with a text
input) prefix it with "+" sign.

You can override q10r templates by creating templates with the same
names in your application's template directory or you can specify
`template` option for desired questionnaires.
