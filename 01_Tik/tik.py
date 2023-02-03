from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def tik_service():
    return 'Hello, I am Tik service!'

@app.route('/tik')
def do_ping():
    tik = 'Tik ...' #???

    response = ''
    try:
        response = requests.get('http://tak-service-container:5001/tak')
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the Tak service.')
        return 'Tik ...\n'

    return 'Tik ... ' + response.text + ' \n'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)