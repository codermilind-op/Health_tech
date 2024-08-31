# symptom_checker/utils.py
import requests

# def fetch_external_data(symptoms):
#     api_url = 'https://databar.ai/'  # Replace with the actual API endpoint
#     # try:
#     response = requests.get(api_url, params={'symptoms': ','.join(symptoms)})
#     if response.status_code == 200:
#         return response.json()
#     return {}

    #     response.raise_for_status()  # Raises an HTTPError for bad responses
    #     return response.json()  # Return the JSON response from the API
    # except requests.RequestException as e:
    #     print(f"An error occurred: {e}")
    #     return {}
# def fetch_external_data(symptoms):
#     api_url = 'https://databar.ai/' # Replace with the actual API endpoint
#     try:
#         response = requests.get(api_url, params={'symptoms': ','.join(symptoms)})
#         print(response.status_code)  # Print status code
#         print(response.text)         # Print response text for debugging
#         response.raise_for_status()  # Raises an HTTPError for bad responses
#         return response.json()      # Return the JSON response from the API
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#         return {}
#     except ValueError as e:  # Handle JSON decode errors
#         print(f"JSON decode error: {e}")
#         return {}

#
# import requests
#
# def fetch_data():
#     api_url = 'https://databar.ai/'  # Replace with your API endpoint
#     try:
#         response = requests.get(api_url)
#         print(f"Status Code: {response.status_code}")
#         print(f"Response Text: {response.text}")
#         if response.status_code == 200:
#             try:
#                 data = response.json()
#                 print("JSON Data:", data)
#             except ValueError:
#                 print("Response is not valid JSON.")
#         else:
#             print(f"Unexpected status code: {response.status_code}")
#     except requests.RequestException as e:
#         print(f"An error occurred: {e}")
#
# fetch_data()


# symptom_checker/utils.py

import requests

def fetch_external_data(symptoms):
    api_url = 'https://api.example.com/conditions'  # Replace with your actual API endpoint
    try:
        response = requests.get(api_url, params={'symptoms': ','.join(symptoms)})
        if response.status_code == 204:  # No Content
            return {}
        response.raise_for_status()
        try:
            return response.json()  # Attempt to parse JSON
        except ValueError:
            print("Response is not valid JSON")
            return {}
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {}

