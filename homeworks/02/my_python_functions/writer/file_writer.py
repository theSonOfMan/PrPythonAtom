import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self.path_ = path
            self.file = None
        
    def _check_path(self, path):
        pass
    
    def print_file(self):
        pass
    
    def write(self, some_string):
        pass
    
    def save_yourself(self, file_name):
        pass
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        pass
