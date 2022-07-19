import requests
import time
import numpy as np
from datetime import datetime
import sys


class CircuitBreaker:
    """ Implement circuit breaker logic for a http client.
    """
    error_list = []

    def __init__(self, http_client, error_threshold, time_window):
        self.http_client = http_client
        self.error_threshold = error_threshold
        self.time_window = time_window

    def do_request(self, method, url, **kwargs):
        try:
            # Circuit breaker logic

            # If a value in the error list is over "time_window" seconds old, then remove the value from the list.
            self.error_list = list(filter(lambda x : x > (datetime.timestamp(datetime.now()) - self.time_window), self.error_list))
            # If the length of the error list is great than the threshold, then we have too many errors in the given time window and the circuit will be opened.
            if len(self.error_list) >= error_threshold:
                print("\33[31mCIRCUIT OPEN: Please wait " +str(self.error_list[error_threshold-1]+self.time_window-datetime.timestamp(datetime.now())) + " seconds to try again.")
                return "Service unavailable, please try again later."
            print("\33[32mCIRCUIT CLOSED: Requests will be forwarded to the microservice.")
            # Make request
            response = requests.request(method, url, **kwargs)
            if response.status_code == 200:
                return str(response.text)
            else:
                raise Exception("ERROR - There was a problem with the request")
        except:
            # The server has thrown and error, so increment the error count.
            self.error_list.append(datetime.timestamp(datetime.now()))
            return "There was a problem with your request. Please resubmit your request."



if __name__ == "__main__":
    client = "http://0.0.0.0:"+sys.argv[1]
    error_threshold = 3
    time_window = 5

    breaker = CircuitBreaker(client, error_threshold, time_window)

    # Good requests
    print("\33[37m" + breaker.do_request("GET" , client, headers=None, data=None))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': '44', 'value2': '13'}))

    # Bad requests
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': 'g'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': 'f3'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': '53'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': '19'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': '23'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': '78'}))
    # Good requests
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': '44', 'value2': '10'}))

    # Wait for circuit breaker to untrip
    time.sleep(6)

    # Bad requests
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': 'hh'}))

    # Good requests
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': '88', 'value2': '45'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': '56', 'value2': '12'}))

    # Bad requests
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': 'hh'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': 'hg'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': 'hg'}))
    print("\33[37m" + breaker.do_request("POST", client+"/sum", headers=None, data={'value1': 'gg', 'value2': 'hg'}))
