#!/bin/bash

# post temporary code to the website
#curl -X POST -H "Content-Type: application/json" -d '{"code":"200", "video":"temp"}' --max-time 1 http://localhost:3001/script-started

# Run the Python script
python3 generate_script.py --topic="circle_are"

# Run the Bash executable
./generate_all_parallel.sh

# Run the narration script
cd narration
python3 narration.py
cd ..
# Link it all together
python3 linker.py

# post the video
#curl -X POST -H "Content-Type: application/json" -d '{"code":"200", "video":"final.mp4"}' http://localhost:3001/script-complete