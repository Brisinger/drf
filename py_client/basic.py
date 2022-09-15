import requests


baseURL = 'http://localhost:8000' # Base url of the REST API
endPoint = f"{baseURL}/api/" # API end point
get_response = requests.post(endPoint, json={"title": "Scissors"})

print(get_response.json()) # Print the response by transforming into python dict
#print(get_response.status_code) # Print status code of httpResponse
#print(get_response.headers) # get headers from response
#print(get_response.text) # Print raw text response
