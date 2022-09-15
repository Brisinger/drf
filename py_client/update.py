import requests
from getpass import getpass


baseURL = 'http://localhost:8000/api' # Base url of the REST API
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
baseURL = 'http://localhost:8000/api/products/41' # Base url of the REST API update product with id:41 
endPoint = f"{baseURL}/update/" # API end point
data = {
    "title" : "New Plate",
    "price": 34,
    "email": "axz@work.com"
}
get_response = requests.put(endPoint, json=data, headers=headers)

print(get_response.json()) # Print the response by transforming into python dict.
print (get_response.status_code) # Status code of response.
#print(get_response.headers) # Print the response headers for API endpoint.