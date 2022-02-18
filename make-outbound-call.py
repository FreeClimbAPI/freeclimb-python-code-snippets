from __future__ import print_function
import time
import freeclimb
from freeclimb.api import default_api
import os
import json
from flask import Flask, request


configuration = freeclimb.Configuration(
    # Defining host is optional and default to https://www.freeclimb.com/apiserver
    host     = "https://www.freeclimb.com/apiserver",
    # Configure HTTP basic authorization: fc
    username = os.environ['ACCOUNT_ID'],
    password = os.environ['API_KEY']
)

# Create an instance of the API class
api_instance = default_api.DefaultApi(freeclimb.ApiClient(configuration))

app = Flask(__name__)

# Triggered locally for convenience
@app.route('/sendCall', methods=['POST'])
def sendCall():
    if request.method == 'POST':
        call_request = freeclimb.MakeCallRequest(
            _from=YOUR_FREECLIMB_NUMBER, to=YOUR_VERIFIED_NUMBER, application_id=YOUR_APP_ID)
        api_instance.make_a_call(make_call_request=call_request)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Specify this route with 'CALL CONNECT URL' in App Config
@app.route('/callConnect', methods=['POST'])
def callConnect():
    if request.method == 'POST':
        script = freeclimb.PerclScript(commands=[
            freeclimb.Say(text="Hello. Welcome to FreeClimb's outbound call tutorial."),
            freeclimb.Pause(length=1000),
            freeclimb.Say(text="Goodbye.")
        ])
        return script.to_json(), 200, {'ContentType': 'application/json'}

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}