from __future__ import print_function
import time
import freeclimb
import os
import json
from flask import Flask, request

configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = os.environ['ACCOUNT_ID']
configuration.password = os.environ['API_KEY']

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"
# Create an instance of the API class
api_instance = freeclimb.DefaultApi(freeclimb.ApiClient(configuration))

app = Flask(__name__)

# Specify this route with 'SMS URL' in App Config
@app.route('/incomingSms', methods=['POST'])
def incomingSms():
    if request.method == 'POST':
        message = "Hello! You texted FreeClimb's Python SDK the following: " + request.json['text']
        message_request = freeclimb.MessageRequest(to=request.json['from'], _from=request.json['to'], text=message)
        api_instance.send_an_sms_message(message_request=message_request)

        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 