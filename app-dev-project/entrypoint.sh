#!/bin/sh
##########################################################################################
##  Summary:
## Since the web service is dependent not only on the container being up and running 
## but also the actual Postgres instance being up and healthy, let's add an entrypoint.
## We referenced the Postgres container using the name of the service, web-db. 
## The loop continues until something like Connection to web-db port 5432 [tcp/postgresql] 
## succeeded! is returned.
##########################################################################################

echo "Waiting for postgres..."

while ! nc -z web-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"
