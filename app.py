from flask import Flask
from os import system as execute

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    execute("cd ~/public/ ")
    execute("git pull ")


if __name__ == '__main__':
    app.run()
