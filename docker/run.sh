#!/bin/bash

docker run --name weather_db  -p 5400:5432 -d personamsolis/solis-db
