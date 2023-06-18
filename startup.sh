#!/bin/bash



# Initialize database
python3 database-init.py

# Run scrapy spider
scrapy crawl sreality

# Run flask server
python3 -m flask run --host=0.0.0.0 --debug --reload
