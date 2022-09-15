import requests
from getpass import getpass


baseURL = 'http://localhost:8000/api'
auth_endpoint = f"{baseURL}/auth/" # API end point
username = input("What is your username?\n") #get user name as input.
password = getpass("What is your password?\n") #get password as input.
auth_response = requests.post(auth_endpoint, json = {"username": username, "password":password})
print("{}".format(auth_response.text)) # Print the token response from obtain_auth_token endpoint.

if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    #add token to Authorization header of request to API.
    headers = {
        "Authorization": "Bearer {}".format(token)
    }

    baseURL = 'http://localhost:8000/api' # Base url of the REST API
    endPoint = f"{baseURL}/products/" # API end point
    get_response = requests.get(endPoint, headers = headers)
    data = get_response.json()
    print(data) # Print the response by transforming into python dict
    next_url = data["next"]
    print(next_url)
    results = data['results']
    print(results)
    # if next_url is not None:
    #     get_response = requests.get(next_url, headers = headers)
    #print(get_response.text) # Print raw text as per content-type specified in response header.
    #print(get_response.headers) # Print the response headers for API endpoint.

