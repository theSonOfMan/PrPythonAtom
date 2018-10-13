import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            print('valid path to file')
            self.path_ = path
            self.file = None
        else:
            print('path not valid')
        
    def _check_path(self, path):
        if os.path.isfile(path):
            return True
        if os.path.isdir(path[:path.rfind('/')]):
            return True
        return False

    def __enter__(self):
        self.file = open(self.path_, 'a')
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
        self.file = None
        return True        

    def print_file(self):
        pass
    
    @property
    def path(self):
        return self.path_

    @path.setter
    def path(self, new_path):
        if self._check_path(new_path):
            self.path_ = new_path
        return None
    
    # def write(self, some_string):
    #     self.file.write(some_string)
    
    def save_yourself(self, file_name):
        data = {'path': self.path_}
        with open(file_name, 'wb') as file:
            pkl.dump(data, file)
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as file:
            data = pkl.load(file)
        return FileWriter(data['path'])
