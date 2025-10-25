#!/bin/bash

cd "$(dirname "$0")/docs"

# Kill any existing process on port 3000
echo "Checking for existing process on port 3000..."
if lsof -ti:3000 > /dev/null 2>&1; then
    echo "Stopping existing server on port 3000..."
    lsof -ti:3000 | xargs kill -9 2>/dev/null || true
    sleep 1
fi

echo "Starting WeHour Docs server..."
python3 server.py
