import json
import os
import fileeditor


class Engine:

    def __init__(self) -> None:
        # dictionary, will be auto generated later
        self.word = None
        self.commands = None

        if os.path.exists("commands.json"):
            self.temp = None
            self.cmds = open('commands.json', )
            self.commands = json.load(self.cmds)
            self.cmds.close()

    def pymrk_generate(self):
        dic = {}
        FileEditor = None

        if os.path.exists("PyMrk") and os.path.exists("PyMrk/Dict") and os.path.exists("PyMrk/Snippets"):
            pass
        else:
            cwd = os.getcwd()
            path = os.path.join(cwd, "PyMrk/Dict")
            os.makedirs(f"{path}")
            path = os.path.join(cwd, "PyMrk/Snippets")
            os.makedirs(f"{path}")

        if not os.path.exists("commands.json"):
            json.dumps(dic, indent=4)

            with open("PyMrk/Dict/commands.json", "w") as outfile:
                json.dump(dic, outfile)

            self.cmds = open('PyMrk/Dict/commands.json', )
            self.commands = json.load(self.cmds)

        FileEdit = fileeditor.FileEditor()

    def run(self, inp):
        if self.commands is not None:
            return
        lines = self.commands[f"{inp}"][str(0)]
        linenum = lines - 1

        for i in range(lines):
            self.word = self.commands[f"{inp}"][str(linenum)]
            print(self.word)
            linenum += 1
