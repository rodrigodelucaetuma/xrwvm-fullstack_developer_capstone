import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030"
)
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)
searchcars_url = os.getenv(
    'searchcars_url',
    default="http://localhost:3050/")


def get_request(endpoint, **kwargs):
    """Send a GET request to the backend with optional query parameters."""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network error: {err}")
        return None
    except ValueError as err:
        print(f"Invalid JSON response: {err}")
        return None


def analyze_review_sentiments(text):
    """Call the sentiment analyzer service for a given text."""
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    """Send a POST request to insert a review into the backend."""
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print("POST URL:", request_url)
        print("POST payload:", data_dict)
        print("Response status:", response.status_code)
        print("Response body:", response.text)
        return response.json()
    except Exception as e:
        print("Network exception:", e)

def searchcars_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key + "=" + value + "&"

    request_url = searchcars_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")
    finally:
        print("GET request call complete!")
