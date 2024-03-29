import json
import os

import requests

import credentials

base_url = "http://127.0.0.1:8000"
image_url = f"{base_url}/api/images/"
pred_image_url = f"{base_url}/api/predimages/"

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
# # print('Image API Response:', response.status_code, response.json())
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# # Sample data for creating an only Image
# image_data = {
#     'image': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_images", "bike_rider.jpg"), 'rb')
# }

# # Send a POST request to create a new Image
# response = requests.post(image_url, auth=(credentials.USERNAME, credentials.PASSWORD), files=image_data)
# # print('Image API Response:', response.status_code, response.json())
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# # Sample data for testing video file only. Should give error.
# image_data = {
#     'video': open(os.path.join(os.getcwd(), "tests", "test_assets", "test_videos", 'he2.mp4'), 'rb')
# }

# # Send a POST request to create a new Image
# response = requests.post(image_url, auth=(credentials.USERNAME, credentials.PASSWORD), files=image_data)
# # print('Image API Response:', response.status_code, response.json())
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# # Sample data for testing null values. Should give error.
# image_data = {
# }

# # Send a POST request to create a new Image
# response = requests.post(image_url, auth=(credentials.USERNAME, credentials.PASSWORD), files=image_data)
# # print('Image API Response:', response.status_code, response.json())
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# Get the latest response from GET request.
# response = requests.get(url = f'{base_url}/api/images/26/', auth=(credentials.USERNAME, credentials.PASSWORD))
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# # GET the POST response that I just did.
# response = requests.get(url = f'{base_url}/api/predimages/47/', auth=(credentials.USERNAME, credentials.PASSWORD))
# print(f"Status code: {response.status_code}")
# json_str = json.dumps(response.json(), indent=4)
# print(json_str)

# # DELETE response should give functionality not found error.
# response = requests.delete(url = f'{base_url}/api/predimages/25/', auth=(credentials.USERNAME, credentials.PASSWORD))
# print(f"Status code: {response.status_code}\n, {response.json()}")
