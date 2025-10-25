#!/bin/bash

cd "$(dirname "$0")/docs"

echo "Starting WeHour Docs server..."
python3 server.py
