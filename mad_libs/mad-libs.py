from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This will be a Mad Libs Machine!'

if __name__ == '__main__':
    app.run()
