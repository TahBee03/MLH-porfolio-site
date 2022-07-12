#!/bin/bash

cd MLH-portfolio-site
git fetch && git reset origin/main --hard > /dev/null
docker compose -f docker-compose.prod.yml down > /dev/null
docker compose -f docker-compose.prod.yml up -d --build > /dev/null
