# this is linter test
# and this is your time

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'


print("hello world")
print("hello world")
print("hello")
print("Mai toh theek hu")
