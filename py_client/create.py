import requests


baseURL = 'http://localhost:8000/api' # Base url of the REST API
endPoint = f"{baseURL}/products/" # API end point

# http://localhost:8000/admin/
# session -> Http Post request data.
# Selenium

headers = {
    "Authorization": "Bearer a486706a9a2d83dfd45d338cf61bf95953078703"
}

data = {
    "title": "Plate234",
    "price": 32.99,
    "email": "abc@work.com"
}
get_response = requests.post(endPoint, json = data, headers = headers)

print(get_response.json()) # Print the response by transforming into python dict
#print(get_response.text) # Print raw text as per content-type specified in response header.
#print(get_response.headers) # Print the response headers for API endpoint.