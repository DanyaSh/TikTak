from flask import Flask
app = Flask(__name__)

@app.route('/')
def tak_service():
    return 'Hello, I am Tak service!'

@app.route('/tak')
def do_tak():
    return 'Tak'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)