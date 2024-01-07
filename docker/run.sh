#!/bin/bash

docker run --name weather_db --rm -p 5400:5432 -d personamsolis/solis-db

sleep 5

docker container logs --tail 50 weather_db

docker container ls -a
