import freeclimb
import os
import requests
import json

configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = os.environ['ACCOUNT_ID']
configuration.password = os.environ['API_KEY']

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"
# Create an instance of the API class
api_instance = freeclimb.DefaultApi(freeclimb.ApiClient(configuration))

first_message = api_instance.list_sms_messages()

next_page_uri = first_message.next_page_uri

all_messages = []
all_messages.extend(map(lambda x: x.to_dict(), first_message.messages))
while(next_page_uri != None):
    next_message = requests.get(url=configuration.host + next_page_uri,
                                auth=(configuration.username, configuration.password))
    all_messages.extend(next_message.json().get('messages'))
    next_page_uri = next_message.json().get('next_page_uri')

file = open("message_results.json", "w")
file.write(json.dumps(all_messages))
file.close()