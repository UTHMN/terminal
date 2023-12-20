import webbrowser
import os

global MainLoop
MainLoop: bool = True

# simple image display
class Engine:
    def __init__(self) -> None:
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,255,0)
    
    def display_contents(self, path):
        webbrowser.open(f"{path}")

def init():
    MainLoop = True

    while MainLoop:

       # creating a new instance
        engine = Engine()

        inp = input('$~')
        
        if inp == "exit":
           MainLoop = False
        else:
            if os.path.isfile(inp):
                engine.display_contents(inp)
            else:
                print("Invalid path")
