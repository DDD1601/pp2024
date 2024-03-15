import threading
import gzip
import pickle
import time

class BackgroundPersistence(threading.Thread):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.data = None
        self.running = True

    def run(self):
        while self.running:
            time.sleep(10)  
            self.save_data()

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def save_data(self):
        if self.data:
            with gzip.open(self.file_path, 'wb') as f:
                pickle.dump(self.data, f)

    def stop(self):
        self.running = False
        self.join()
