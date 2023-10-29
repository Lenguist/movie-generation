import openai
import os
import uuid
import json
from utils import get_oai_completion
import argparse

# parser = argparse.ArgumentParser(description='Generate a scene based on a specified topic and file.')

# # Add arguments
# parser.add_argument('--topic', required=True, help='The topic for the scene.')

# # Parse arguments
# args = parser.parse_args()

# Access arguments
topic = ""
"""
def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False
"""

if __name__ == "__main__":
    idea_prompt = """
    Generate script for an episode of a TV show "Two Broke Girls".
    """ % topic

    messages = [
            {"role": "system", "content": idea_prompt},
    ]

    acts = get_oai_completion(messages)
    # Convert the string into a list of dictionaries
    print(acts)
"""
    data_list = json.loads(acts)

    # Directory to save the files in
    directory = topic.replace(" ", "_")

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

# Save each dictionary into a separate .json file
for entry in data_list:
    filename = os.path.join(directory, entry["scene-filename"] + ".json")
    with open(filename, "w") as file:
        json.dump(entry, file, indent=4)

# generate buffer file topic.txt that other files can use to get topic
with open("topic.txt", "w") as f:
    f.write(directory)
"""
