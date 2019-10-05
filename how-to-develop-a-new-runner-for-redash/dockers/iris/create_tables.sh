#!/usr/bin/env bash

cd ~/redash 

sleep 60
# Create tables
docker-compose run --rm server create_db

# Create database for tests
docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"

bash