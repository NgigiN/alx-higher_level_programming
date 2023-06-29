#!/usr/bin/bash

response=$(curl -sI "$1")

body_size=$(echo $response | wc -c)

echo "$body_size"
