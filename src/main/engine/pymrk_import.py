import json

global my_dict
my_dict = {}

def pymrk_import(self, import_path):
    to_path = import_path + "commands.json"
    f = open (to_path, "r")
    data = json.loads(f.read())
    
    for i in data:
        my_dict[i] = data[i] # replace my_dict with dict to load into
    
pymrk_import("", "./PyMrk/Dict/")
print(my_dict)