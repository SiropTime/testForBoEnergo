from flask import Flask

from api import api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def index():
    return 'index page'


