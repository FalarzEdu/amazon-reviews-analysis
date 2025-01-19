#!/bin/bash
mongoimport --username "$MONGO_INITDB_ROOT_USERNAME" \
            --password "$MONGO_INITDB_ROOT_PASSWORD" \
            --authenticationDatabase "admin" \
            --db amazon_reviews \
            --collection reviews \
            --file /data/reviews.json \
            --jsonArray