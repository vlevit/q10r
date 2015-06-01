import logging

from flask import Flask

from q10r import q10r


app = application = Flask(__name__)
app.config.from_pyfile('example_config.py')
app.register_blueprint(q10r)


if __name__ == '__main__':
    app.run()
