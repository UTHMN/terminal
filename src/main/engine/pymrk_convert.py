import os

def pymrk_convert(self, dir_path):
    files = os.listdir(dir_path)
    
    for i in range(len(files)):
        file_path = dir_path + files[i]
        
        with open(file_path, 'r') as file:
            file_content = file.read()
    
pymrk_convert("", "./PyMrk/Snippets/")