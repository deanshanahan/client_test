#!/usr/bin/env bash

docker build -t microservice ./microservice/
docker build -t circuitbreaker ./circuitbreaker/
docker run -t -p 8080:5000 microservice
