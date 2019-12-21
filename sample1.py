from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/sample1')


# def running():
#     return 'Hello Kho'

def running2():
    return 'aigo'

app.run(debug=True)