import os
import json
import datetime



# Create a sample JSON data (you can replace this with your data)
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}



def conn_private_node(private_node_addrss, data):
    # Specify the path where you want to create the file
    folder_path = f"{os.getcwd()}/Connection/Private_Node/{private_node_addrss}"

    # Ensure the folder exists, create it if it doesn't
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generate a filename based on the current timestamp
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    formatted_timestamp = timestamp.strftime("GMT-%Y_%m_%d-%H:%M:%S:%f")

    # Replace ':' and '.' with '-' to meet the file naming requirements
    file_name = formatted_timestamp.replace(':', '-').replace('.', '-') + ".json"

    # Specify the full path of the JSON file to be created
    file_path = os.path.join(folder_path, file_name)

    # Write the JSON data to the file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON file '{file_name}' created at '{folder_path}'.")


conn_private_node('webe+2@gmail.com', data)
    
