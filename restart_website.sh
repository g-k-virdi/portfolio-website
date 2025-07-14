#!/bin/bash

echo "Stopping any running Flask processes..."
pkill -f "python.*app.py" || echo "No Flask processes found to kill."

echo "Starting the website..."
cd "$(dirname "$0")"
echo "Running from directory: $(pwd)"
python app.py &

echo "Website started at http://localhost:4000"
echo "Press Ctrl+C to stop the script" 