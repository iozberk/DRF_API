import requests

endpoint = 'https://www.httpbin.org/status/200/'
endpoint = 'https://www.httpbin.org/anything'
endpoint = 'http://localhost:8000/api'
get_response = requests.get(endpoint, json={'product_id': 123}) # HTTP Request

# print(get_response.text) # raw text response

print(get_response.json())
# print(get_response.status_code)






