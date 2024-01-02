#!/bin/bash

docker container run --name weather_db --rm -p 5433:5432 -d personamsolis/solis-db
