import json
import requests
import os

from dotenv import load_dotenv


# this function will login into the API for UKG Ready and return the token provided
# if there is an error it will print out the error instead
# the function requires that the API key is passed into it as well as the username, password, and company short name
# Any call made after the initial login will use the token that this function returns.
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

    # if there is data sent back, and that data contains a token
    # then return the aforementioned token
    if json_data and 'token' in json_data:
        return json_data.get('token')


# this function needs the company short name and the token to be passed in as parameters
# the function will then send a get request for all the cost centers in UKG
def get_cost_centers(short_name, token):
    # header being sent to the API
    my_headers = {'Authentication': 'Bearer ' + token, 'Content-Type': 'application/json'}

    # API response
    response = requests.get(
        'https://secure.saashr.com/ta/rest/v2/companies/!' + short_name + '/config/cost-center-jobs',
        headers=my_headers)

    # store JSON data that was received and make sure that we got a 200 OKAY http repsonse
    json_data = response.json() if response and response.status_code == 200 else print("the status code for the get "
                                                                                       "request was not 200")
    # holds all of the names of the cost centers
    names = []

    # this for loop goes through the JSON data looking for visible cost center names
    for item in json_data['costCenterJobs']:
        if json.dumps(item['visible']) == "true":
            names.append(item['name'])

    # return the names that we stored earlier
    return names


# this function send a post request to the API that creates new branches on the cost center tree
# it requires the company short name, the token from logging into the API,
# the length of the content being sent and the name of the cost center we are adding a branch to
def post_cost_center_names(short_name, token, content_length, name):

    # the header being sent to the API
    my_headers = {'Authentication': 'Bearer ' + token, 'Content-Type': 'application/json',
                  'Content-Length': content_length}

    # the payload that contains the JSON object we want to use to create the new branches
    payload = {'cost_centers': {
        'parent_cc': {
            'tree_index': 1
        },
        'name': name,
    }
    }

    # receives the response from the API
    response = requests.post(
        'https://secure.saashr.com/ta/rest/v2/companies/!' + short_name + '/config/cost-centers/collection',
        headers=my_headers,
        json=payload)

    # prints the status code
    print(response.status_code)

    # prints the entire response
    print(response.json())


# loads the .env file into the program
load_dotenv('key.env')

# all of these environment variables are loaded from the .env file
API_KEY = os.environ.get('PROJECT_API_KEY')
USERNAME = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
SHORT_NAME = os.environ.get('SHORT_NAME')

# store the token that we get by logging into the API
TOKEN = login_api(API_KEY, USERNAME, PASSWORD, SHORT_NAME)

# collect the cost center names into a variable called "data"
data = get_cost_centers(SHORT_NAME, TOKEN)
