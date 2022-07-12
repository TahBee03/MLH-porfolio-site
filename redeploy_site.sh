#!/bin/bash

cd MLH-portfolio-site
git fetch && git reset origin/main --hard > /dev/null
docker compose -f docker_compose.prod.yml down > /dev/null
docker compose -f docker_compose.prod.yml up -d --build > /dev/null
cp redeploy_site.sh ..
