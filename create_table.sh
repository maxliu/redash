#!/usr/bin/env bash


docker-compose run --rm server create_db && docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"""
