from flask import Flask, jsonify
from os import system as execute

app = Flask(__name__)
app.debug = False


@app.route('/git/pull/')
def hello_world():  # put application's code here
    execute("cd ~/public/ ")
    execute("git pull ")
    return jsonify(detail='success')


if __name__ == '__main__':
    app.run()
