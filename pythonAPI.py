import flask
import requests
import yaml
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

@app.route('/health', methods=['GET'])
def health():
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    return "Automate All The Things " + current_time  



app.run(host='0.0.0.0')
