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

# Specify this route with 'SMS URL' in App Config
@app.route('/incomingSms', methods=['POST'])
def incomingSms():
    if request.method == 'POST':
        message = "Hello! You texted FreeClimb's Python SDK the following: " + request.json['text']
        message_request = freeclimb.MessageRequest(_from=request.json['from'], to=request.json['to'], text=message)
        api_instance.send_an_sms_message(message_request=message_request)

        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
