import requests


baseURL = 'http://localhost:8000/api/products' # Base url of the REST API
endPoint = f"{baseURL}/37/" # API end point
get_response = requests.get(endPoint)

print(get_response.json()) # Print the response by transforming into python dict
print (get_response.status_code) # Status code of response.