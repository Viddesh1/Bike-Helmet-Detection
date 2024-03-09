import requests
import os

base_url = 'http://127.0.0.1:8000'
image_url = f'{base_url}/api/images/'
pred_image_url = f'{base_url}/api/predimages/'
USERNAME = 'viddesh'
PASSWORD = '!@#$%^&*()_+'

# response = requests.get(url = f'{base_url}/api/images/20/', auth=(USERNAME, PASSWORD))
# print(response.json())

# response = requests.get(url = f'{base_url}/api/predimages/15/', auth=(USERNAME, PASSWORD))
# print(response.json())


# # Sample data for creating an Image
# image_data = {
#     'image': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_images", "bike_rider.jpg"), 'rb'),
#     'video': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_videos", 'he2.mp4'), 'rb')
# }

# # Send a POST request to create a new Image
# response = requests.post(image_url, auth=(USERNAME, PASSWORD), files=image_data)
# print('Image API Response:', response.status_code, response.json())

# # Get the response from GET request.
# response = requests.get(url = f'{base_url}/api/images/25/', auth=(USERNAME, PASSWORD))
# print(response.json())

# # POST response that I just did.
# response = requests.get(url = f'{base_url}/api/predimages/25/', auth=(USERNAME, PASSWORD))
# print(f"Status code: {response.status_code}\n, {response.json()}")

# # DELETE response should give error.
# response = requests.delete(url = f'{base_url}/api/predimages/25/', auth=(USERNAME, PASSWORD))
# print(f"Status code: {response.status_code}\n, {response.json()}")

# Test using authentication token.
# # Send a POST request to create a new Image
# response = requests.post('http://127.0.0.1:8000/api/auth/login/', auth=(USERNAME, PASSWORD))
# print('Image API Response:', response.status_code, response.json())

# Testing token
# import requests

# # Base URL of your Django server
# base_url = 'http://127.0.0.1:8000'

# # Token received from the login response
# token = '3109493ba3fd27de49df87225cd9e76979bdc319ea4819650df0e23344efa29a'

# # Set the Authorization header with the token
# headers = {'Authorization': f'Token {token}'}

# # Send a GET request to a protected endpoint
# response = requests.get(f'{base_url}/api/images/20/', headers=headers)

# print(response.status_code)
# print(response.json())

from knox.auth import TokenAuthentication
from knox.models import AuthToken

token = 'your_token_here'
token_object = AuthToken.objects.filter(token_key=token).first()

if token_object and TokenAuthentication().decode_token(token):
    print("Token is valid")
else:
    print("Token is invalid")




# import requests
# import os

# # Base URL of your Django server
# base_url = 'http://127.0.0.1:8000'

# # Obtain an authentication token
# response = requests.post(f'{base_url}/api/token/', data={'username': 'viddesh', 'password': '!@#$%^&*()_+'})
# token = response.json()['access']

# # Set the authentication token in the request headers
# # headers = {'Authorization': f'Bearer {token}'}

# # Sample data for creating an Image
# image_data = {
#     'image': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_images", "bike_rider.jpg"), 'rb'),
#     'video': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_videos", 'he2.mp4'), 'rb')
# }





# import requests
# import os

# # Base URL of your Django server
# base_url = 'http://127.0.0.1:8000'

# # Endpoint for the Image API
# image_url = f'{base_url}/api/images/'

# # Endpoint for the PredImage API
# pred_image_url = f'{base_url}/api/predimages/'

# # Send a POST request to create a new Image
# response = requests.post(image_url, data={'username': 'viddesh', 'password': '!@#$%^&*()_+'}, files=image_data)
# print('Image API Response:', response.status_code, response.json())

# # Send a GET request to retrieve all Images
# response = requests.get(image_url)
# print('All Images API Response:', response.status_code, response.json())

# # Send a GET request to retrieve a specific Image by ID
# response = requests.get(f'{image_url}1/')
# print('Single Image API Response:', response.status_code, response.json())

# # Send a PUT request to update an Image by ID
# response = requests.put(f'{image_url}1/', files=image_data)
# print('Update Image API Response:', response.status_code, response.json())

# # Send a DELETE request to delete an Image by ID
# response = requests.delete(f'{image_url}1/')
# print('Delete Image API Response:', response.status_code, response.json())

# # Send a POST request to create a new PredImage
# response = requests.post(pred_image_url, data={'pred_image_id': 1})
# print('PredImage API Response:', response.status_code, response.json())

# # Send a GET request to retrieve all PredImages
# response = requests.get(pred_image_url)
# print('All PredImages API Response:', response.status_code, response.json())

# # Send a GET request to retrieve a specific PredImage by ID
# response = requests.get(f'{pred_image_url}1/')
# print('Single PredImage API Response:', response.status_code, response.json())

# # Send a PUT request to update a PredImage by ID
# response = requests.put(f'{pred_image_url}1/', data={'pred_image_id': 2})
# print('Update PredImage API Response:', response.status_code, response.json())

# # Send a DELETE request to delete a PredImage by ID
# response = requests.delete(f'{pred_image_url}1/')
# print('Delete PredImage API Response:', response.status_code, response.json())
