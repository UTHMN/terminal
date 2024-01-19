import json
import os

class Engine:
    def __init__(self) -> None:
        self.commands = {}
        self.pymrk_initialize()
        
    def debug_mode(self):
        try:
            inp = input("$~")
            exec(inp)

        except Exception as error:
            print(error)
            
    def pymrk_convert(self):
        files = os.listdir("./PyMrk/Snippets/")

        for i in range(len(files)):
            file_path = "./PyMrk/Snippets/" + files[i]
        
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.commands[files[i]] = file_content
            file.close()
                
    def pymrk_export(self):
        to_export = "PyMrk/Dict/commands.json"

        with open(to_export, "w") as outfile:
            json.dump(self.commands, outfile, indent=4)
        outfile.close()
    
    def pymrk_import(self):
        to_path = "./PyMrk/Dict/commands.json"
        f = open (to_path, "r")
        data = json.loads(f.read())
    
        for i in data:
            self.commands[i] = data[i]
            
    def pymrk_initialize(self):
        if os.path.exists("PyMrk") and os.path.exists("PyMrk/Dict") and os.path.exists("PyMrk/Snippets"):
            pass
        else:
            cwd = os.getcwd()
            path = os.path.join(cwd, "PyMrk/Dict")
            os.makedirs(f"{path}")
            path = os.path.join(cwd, "PyMrk/Snippets")
            os.makedirs(f"{path}")
            
    def run(self, cmd):
        try:
            self.word = self.commands[f"{cmd}"]
            exec(str(self.word))
        
            return str(self.word)

        except Exception as error:
            return error
