import os
import time
import shutil

# Define the source folder (unprocessed) and destination folder (processed)
source_folder = '/Users/alessandro.rea/Desktop/scint-private-node/Data/_STM/Queues/st_0/_Core'
destination_folder = '/Users/alessandro.rea/Desktop/scint-private-node/Data/_STM/Queues/st_1/_Core'

while True:
    # Get a list of files in the source folder
    files = os.listdir(source_folder)
    
    # Iterate through the files
    for filename in files:
        source_path = os.path.join(source_folder, filename)
        
        # Check if it's a file (not a subdirectory)
        if os.path.isfile(source_path):
            # Open and print the file's contents
            with open(source_path, 'r') as file:
                content = file.read()
                print("File:", filename)
                print("Content:\n", content)
                
                # Move the file to the destination folder
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved to {destination_path}")
    
    print('finished now :-)')
    # Wait for 10 seconds before checking again
    time.sleep(10)