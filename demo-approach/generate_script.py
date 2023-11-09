import openai
import os
import uuid
import json
from utils import get_oai_completion
import argparse
from datetime import datetime



# Now, you can save your generated scripts in this folder.


# parser = argparse.ArgumentParser(description='Generate a scene based on a specified topic and file.')

# # Add arguments
# parser.add_argument('--topic', required=True, help='The topic for the scene.')

# # Parse arguments
# args = parser.parse_args()

# Access arguments
topic = """
Digital Shadows:
A talented young cybersecurity expert
discovers a mysterious encrypted message
on her university's network. As she decodes it,
she realizes it's a cry for help from someone
trapped in a digital prison. She races against
time to rescue this digital entity while evading
a secret society that wants to keep this technology hidden.
"""


if __name__ == "__main__":
    idea_prompt = """
    Generate a short story based on the following premise: %s.
    Make sure your generation is at most 2000 words long
    """ % topic

    messages = [
            {"role": "system", "content": idea_prompt},
    ]

    acts = get_oai_completion(messages)

# Function to create a folder named with the current date and time
def create_folder():
    now = datetime.now()
    folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(folder_name)
    return folder_name

# Function to create a text file with a title
def create_text_file(folder_name, title):
    # Replace spaces with underscores and make all letters lowercase
    sanitized_title = title.split(' ')[:2].join("_").lower()
    file_name = f"{sanitized_title}.txt"

    # Combine the folder name and the file name to get the full path
    full_path = os.path.join(folder_name, file_name)

    # Create the text file and write some content (or leave it empty)
    with open(full_path, "w") as f:
        f.write(acts)


folder_name = create_folder()
create_text_file(folder_name, topic)



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

"""
def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except json.JSONDecodeError:
        return False
"""