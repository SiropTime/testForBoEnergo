from flask import Flask

from api import api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    # app.env = 'development'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, port=8080, host="0.0.0.0")
