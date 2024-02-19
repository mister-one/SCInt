import os


def list_files_in_queue(queue_name='Inbound'):
    files_in_queue=[]
    directory_path = os.path.join('Data/_Void/Queues', queue_name)
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            files_in_queue.append(os.path.join(directory_path, filename))
    return files_in_queue
