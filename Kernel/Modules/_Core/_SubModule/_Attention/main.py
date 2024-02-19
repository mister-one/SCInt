import os
import time
import shutil

# Define the source folder (unprocessed) and destination folder (processed)
source_folder = '/Users/alessandro.rea/Desktop/scint-private-node/Data/_STM/Queues/st_0/_Core'
destination_folder = '/Users/alessandro.rea/Desktop/scint-private-node/Data/_STM/Queues/st_1/_Core'


class Attention:
    def __init__(self) -> None:
        self.name = 'Attention'
        self.objective = 'Decide if somthig is worth my attention'


    def execute(self):
        return f'EXECUTED {self.name} (Now, Later, Never)'