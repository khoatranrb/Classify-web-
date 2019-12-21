from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/main', methods = ['POST'])

def get_message():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Message: '+name+' !'
    }
    return jsonify(response)

app.run(debug=True)