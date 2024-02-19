import json
import os
import queue
import threading
import time

class ShortTermMemory:
    _is_first_instance = True

    def __init__(self, topic_channel="_Core"):
        
        # Check if this is the first time the class is being instantiated
        if ShortTermMemory._is_first_instance:
            ShortTermMemory._is_first_instance = False
            topic_folder = os.path.join(os.getcwd(), topic_channel)
            if not os.path.exists(topic_folder):
                os.makedirs(topic_folder)
            topic_folder = os.path.join(os.getcwd(), topic_channel)
        else:
            pass

        # Rest of your initialization logic here
        self.topic_channel = topic_channel
        self.queue = queue.Queue()

    def publish_event(self, event_data):
        # Create a new file in the topic folder
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{len(os.listdir(self.topic_channel)) + 1}.json"
        file_path = os.path.join(self.topic_channel, filename)

        with open(file_path, 'w') as file:
            file.write(json.dumps(event_data))

        # Add the file path to the processing queue
        self.queue.put(file_path)

    def process_file(self, file_path):
        # Placeholder for file processing logic
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Processing file: {file_path}, Content: {content}")
        os.remove(file_path)

    def execute(self):
        while True:
            try:
                # Get all files in the topic folder
                files = [f for f in os.listdir(self.topic_channel) if os.path.isfile(os.path.join(self.topic_channel, f))]

                # Process each file
                for file_name in files:
                    file_path = os.path.join(self.topic_channel, file_name)
                    self.process_file(file_path)

            except Exception as e:
                print(f"Error processing files: {e}")
            time.sleep(5)  # Add a delay to avoid constant checking

    




# file_queue = ShortTermMemory(topic_channel="#resorcemonitoring")


# file_monitor_thread = threading.Thread(target=file_queue.execute, daemon=True)
# file_monitor_thread.start()

# # Publish events to the file queue
# event_data1 = {"key1": "value1"}
# file_queue.publish_event(event_data1)

# file_queue.execute()

# event_data2 = {"key2": "value2"}
# file_queue.publish_event(event_data2)

# # Sleep for a while to allow the file monitoring thread to process the events
# time.sleep(2)