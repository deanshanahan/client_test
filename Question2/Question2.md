2. Implement a circuit Breaker

You are tasked with writing a library that implements the circuit breaker pattern to make HTTP clients more resilient to failure, e.g. 500 error or timeouts.

Please implement a small library that wraps and invokes an HTTP client; the HTTP client can be mocked out for this implementation. The library should take in 2 inputs: a time window (in seconds) and an error threshold. If the number of errors from the wrapped HTTP client exceeds the error threshold, the library should prematurely return an error, e.g. “CircuitOpenError”. Whenever the number of errors falls below the threshold, the circuit should be closed and requests should flow freely.

You may think to implement error-counting with a simple scalar. Doing so would be a good first iteration. If you have the time, we’d like you to implement a rolling window with an appropriate backing data structure. The backing data structure used to bookkeep failures within a time window is crucial to an efficient solution. However, your solution does not need to be optimal. Please demonstrate a working solution with a test case or by printing to stdout.

This exercise should take no more than 45 minutes of coding time + time for a little polish. Please push your solution to GitHub or Gitlab for us to review!

---

Please do the following to replicate my testing:

1. Navigate to `./Question2`.
1. Run `bash ./setup_script.sh`. This will build the microservice and circuitbreaker images and start the microservice with the tty outputting to the terminal window. This allows you to see `200 OK` and `500 Internal Server Error` status codes clearly.
1. To run the circuitbreaker, run the command `docker run -t --net=host circuitbreaker:latest python main.py 8080` in a different terminal. You will see green text for when the circuit breaker is closed (allowing traffic), red text for when the circuit break is open (disallowing traffic), and white text for responses. The response `Service unavailable, please try again later.` means that the circuit breaker does not forward requests to the microservice at all, while `There was a problem with your request. Please resubmit your request.` indicates that the microservice received the request but could not process it.

*Note: the value for error_threshold, and for time_window are hardcoded in the main.py file.*

The microservice will return a 500 error when it receives a request that it cannot process. The microservice has a basic health check and a post endpoint for finding the sum of two values. To generate errors, I am sending letters instead of numeric values to the service, the causes the service to return a 500 error.
