from flask import Flask, jsonify
from os import system as execute

app = Flask(__name__)
app.debug = False


@app.route('/git/pull/', methods=['POST', ])
def hello_world():  # put application's code here
    execute("bash ~/.scripts/pull.sh")
    return jsonify(detail='success')


if __name__ == '__main__':
    app.run()
