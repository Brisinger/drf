import requests


product_id = input("What is the product is you wish to delete? \n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not a valid product id.")

if product_id:
    baseURL = 'http://localhost:8000/api/products' # Base url of the REST API
    endPoint = f"{baseURL}/{product_id}/delete/" # API end point

    get_response = requests.delete(endPoint)

    #print(get_response.headers) # Print the response header details.
    print (get_response.status_code, get_response.status_code == 204) # Status code of response.
    #print(get_response.header