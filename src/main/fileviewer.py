import climage
import os

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

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

    def render_image(self, path):
        output = climage.convert(f'{path}', True, False, True)
        print(output)
    
    def display_contents(self, path):
        print("")
        with open(f'{path}', 'r') as f:
            print(f.read())
        print("")

def init():
    MainLoop = True

    while MainLoop:

       # creating a new instance
        engine = Engine()

        inp = input('$~')

        if inp.endswith('.jpg') or inp.endswith('.jpeg') or inp.endswith('.png') or inp.endswith('.gif'):
            if os.path.isfile(inp):
                engine.render_image(inp)
            else:
                print("Invalid path")
        elif inp == "exit":
           os.system('cls' if os.name == 'nt' else 'clear')
           MainLoop = False
        else:
            if os.path.isfile(inp):
                engine.display_contents(inp)
            else:
                print("Invalid path")
