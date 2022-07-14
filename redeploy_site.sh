#!/bin/bash

cd MLH-portfolio-site
git fetch && git reset origin/main --hard
docker compose -f docker_compose.prod.yml down
docker compose -f docker_compose.prod.yml up -d --build
cp redeploy_site.sh ..
