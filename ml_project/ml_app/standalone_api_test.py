import requests
import os
import json
import credentials

base_url = 'http://127.0.0.1:8000'
image_url = f'{base_url}/api/images/'
pred_image_url = f'{base_url}/api/predimages/'

# http://127.0.0.1:8000/api/

# response = requests.get(url = f'{base_url}/api/', auth=(credentials.USERNAME, credentials.PASSWORD))
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# response = requests.get(url = f'{base_url}/api/images/20/', auth=(credentials.USERNAME, credentials.PASSWORD))
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# response = requests.get(url = f'{base_url}/api/predimages/15/', auth=(credentials.USERNAME, credentials.PASSWORD))
# print(response.json())

# response = requests.get(url = f'{base_url}/api/predimages/', auth=(credentials.USERNAME, credentials.PASSWORD))
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# # Sample data for creating an Image
# image_data = {
#     'image': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_images", "bike_rider.jpg"), 'rb'),
#     'video': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_videos", 'he2.mp4'), 'rb')
# }

# # Send a POST request to create a new Image
# response = requests.post(image_url, auth=(credentials.USERNAME, credentials.PASSWORD), files=image_data)
# print('Image API Response:', response.status_code, response.json())
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# Get the latest response from GET request.
# response = requests.get(url = f'{base_url}/api/images/26/', auth=(credentials.USERNAME, credentials.PASSWORD))
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# GET the POST response that I just did.
# response = requests.get(url = f'{base_url}/api/predimages/26/', auth=(credentials.USERNAME, credentials.PASSWORD))
# print(f"Status code: {response.status_code}\n, {response.json()}")
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# DELETE response should give error.
# response = requests.delete(url = f'{base_url}/api/predimages/25/', auth=(credentials.USERNAME, credentials.PASSWORD))
# print(f"Status code: {response.status_code}\n, {response.json()}")



####################################################

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
