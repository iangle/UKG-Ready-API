import json

import requests
import os


from dotenv import load_dotenv


# this function will login into the API for Kronos and return the token provided
# if there is an error it will print out the error instead
# the function requires that the API key is passed into it as well as the username, password, and company short name
def login_api(api_key, username, password, short_name):
    # the header being sent to the API
    my_headers = {'Content-Type': 'application/json', 'api-key': api_key}

    # the payload being sent to the API
    payload = {"credentials": {
        "username": username,
        "password": password,
        "company": short_name
    }
    }

    # The response that is sent back from the API
    response = requests.post('https://secure.saashr.com/ta/rest/v1/login',
                             headers=my_headers,
                             json=payload)

    # code from: https://stackoverflow.com/questions/43480466/how-to-parse-json-data-from-api-response-in-python
    json_data = response.json() if response and response.status_code == 200 else print(
        "the status code for logging in was not 200")

    if json_data and 'token' in json_data:
        return json_data.get('token')


def get_cost_centers(short_name, token):

    my_headers = {'Authentication': 'Bearer ' + token, 'Content-Type': 'application/json'}

    response = requests.get('https://secure.saashr.com/ta/rest/v2/companies/!' + short_name + '/config/cost-center-jobs',
                            headers=my_headers)

    json_data = response.json() if response and response.status_code == 200 else print("the status code for the get "
                                                                                       "request was not 200")

    names = []

    for item in json_data['costCenterJobs']:
        if json.dumps(item['visible']) == "true":
            names.append(item['name'])

    return names


def put_cost_center_names(short_name, token, content_length, name, id):

    my_headers = {'Authentication': 'Bearer ' + token, 'Content-Type': 'application/json',
                  'Content-Length': content_length}

    payload = {'cost_centers': {
        'parent_cc': {
            'tree_index': 1
        },
        'name': name,
        }
    }

    response = requests.post('https://secure.saashr.com/ta/rest/v2/companies/!' + short_name + '/config/cost-centers/collection',
                            headers=my_headers,
                            json=payload)

    print(response.status_code)

    print(response.json())


load_dotenv('key.env')

API_KEY = os.environ.get('PROJECT_API_KEY')

USERNAME = os.environ.get('USER')

PASSWORD = os.environ.get('PASSWORD')

SHORT_NAME = os.environ.get('SHORT_NAME')

TOKEN = login_api(API_KEY, USERNAME, PASSWORD, SHORT_NAME)

POSITION_ID = "21556495044"

data = get_cost_centers(SHORT_NAME, TOKEN)

#for item in data:
#    print(item)

#for item in data:
#    put_cost_center_names(SHORT_NAME, TOKEN, "1", item, POSITION_ID)
