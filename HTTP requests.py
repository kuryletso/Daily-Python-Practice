# Excercise: https://www.hackinscience.org/exercises/doing-http-requests
#
#
# Solution:

import requests 

try:
    response = requests.get('https://api.github.com/users/python', timeout=60) 
    response.raise_for_status() 
    print(response.content)
except requests.exceptions.ConnectionError:
    print("No internet connectivity.")
except requests.exceptions.HTTPError:
    print(f"Bad response, status code: {response.status_code}")