import os
import json

folder_path = "/Users/alessandro.rea/Desktop/UnitTesting/Queues/_Core"

# Get a list of all JSON files in the folder, sorted by modification time (newest to oldest)
json_files = sorted(
    [
        os.path.join(folder_path, filename)
        for filename in os.listdir(folder_path)
        if filename.endswith(".json")
    ],
    key=lambda f: os.stat(f).st_mtime,
    reverse=True,
)

# # Loop through the sorted list of JSON files and open each one
# for file_path in json_files:
#     with open(file_path) as json_file:
#         json_data = json.load(json_file)
#         # Do something with the JSON data here

for file_path in json_files:
    print(file_path)


for file_path in json_files:
    with open("/Users/alessandro.rea/Desktop/UnitTesting/Queues/_Core/GMT-2023_01_25-12:12:16:937291.json") as json_file:
        json_data = json.load(json_file)
print(json_data)