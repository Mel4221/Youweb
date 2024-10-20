#!/bin/bash

bash build.sh &&
sudo docker build -t youweb:lastest . &&
sudo docker run -p 127.0.0.1:8080:8080 youweb:latest