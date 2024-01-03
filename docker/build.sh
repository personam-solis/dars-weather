#!/bin/bash


docker build --rm -t personamsolis/solis-db:development .
docker build --rm  -t personamsolis/solis-db:latest .
# docker image push personamsolis/solis-db:development
# docker image push personamsolis/solis-db:latest
