import time
import socket
import getpass
import sys
import os
import winsound as ws
import turtle
import pyperclip

global iNav
iNav = False


# def
def callback():
    # init
    start_time = time.time()
    querySuccess = 0
    c = input(socket.gethostname() + "@" + getpass.getuser() + ": ")

    # cmds

    # circle :O
    if c == "circle :0":
        turtle.circle(50)
        querySuccess = 1
        turtle.exitonclick()
        print("DO NOT REOPEN")

    # rectangle :[]
    if c == "square :[]":
        turtle.shape("square")
        turtle.exitonclick()
        querySuccess = 1
        print("DO NOT REOPEN")

    # print command
    if c == "print":
        i = input("query: ")
        print(i)
        querySuccess = 1

    # exit terminal
    if c == "exit" or c == "quit":
        ws.PlaySound("SystemExit", ws.SND_ASYNC)
        querySuccess = 1
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

    # benchmarking tool
    if c == "benchmark":
        fps = (1.0 / (time.time() - start_time)) * 100
        print("FPS: ", round(fps, 2))
        print(f"Cpu Cores: {os.cpu_count()}")
        print(f"Operating System: {os.name}")
        querySuccess = 1

    # cmds list
    if c == "help":
        print("STANDALONE COMMANDS:")
        print("help                 Displays list of commands")
        print("benchmark            Runs a benchmarking application")
        print("exit                 Exits the terminal")
        print("print                Prints the given query")
        print("Clear                Clear the terminal")
        print("PATH TOOLSET:")
        print("path --edit          Edits a given file")
        print("path --open          Opens a given file")
        print("path --print         Prints a given file")
        print("path --properties    Finds properties of a file")
        print("path --find          Finds if given file exists")
        print("path --remove        Removes a file at a given path")
        print("path --list          Lists the contents of a directory at a given path")
        print("path --add           Adds a file at a given directory")
        print("path --current       Displays the current path you are running")
        print("path --size          Displays the size of a path in megabytes")
        print("path --nav           Lets you navigate to a certain path and copies it to the clipboard")
        querySuccess = 1

    # clear terminal

    if c == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        querySuccess = 1

    # path toolset

    if c == "path --nav":
        print(os.listdir("C:/"))
        tPath = "C:/"
        temp = tPath
        iNav = True
        while iNav:
            Cpath = input("path: ")
            if Cpath == "exit":
                tPath = temp + Cpath
                temp = tPath + "/"
                pyperclip.copy(f"{tPath}")
                print("successfully copied to clipboard")
                iNav = False
            else:
                if os.path.exists(f"{Cpath}"):
                    tPath = temp + Cpath
                    print(os.listdir(tPath))
                    temp = tPath + "/"
                else:
                    print("path does not exist, you may continue")
                    tPath = temp + Cpath
                    temp = tPath + "/"

    querySuccess = 1

    if c == "path --size":
        pathSize = input("Directory path to be read: ")
        if os.path.exists(f"{pathSize}"):
            peth = os.path.getsize(f'{pathSize}') / 100
            print(f'{pathSize} is {peth} gigabytes')
        else:
            print("Error: path does not exist")
        querySuccess = 1

    if c == "path --current":
        if os.path.exists(f"{os.getcwd()}"):
            print(f'Current directory: {os.getcwd()}')
        else:
            print("Error: file does not exist")
        querySuccess = 1

    if c == "path --add":
        pathAdd = input("Directory path to be created: ")
        os.makedirs(f"{pathAdd}")
        querySuccess = 1

    if c == "path --list":
        pathList = input("Directory path to be listed: ")
        if os.path.exists(f"{pathList}"):
            print(os.listdir(f"{pathList}"))
        else:
            print("Error: file does not exist")
        querySuccess = 1

    if c == "path --remove":
        pathRemove = input("Directory path to be removed: ")
        if os.path.exists(f"{pathRemove}"):
            os.remove(f"{pathRemove}")
        else:
            print("Error: directory does not exist")
        querySuccess = 1

    if c == "path --open":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "open")
        else:
            print("Error: file does not exist")
        querySuccess = 1

    if c == "path --print":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "print")
        else:
            print("Error: file does not exist")
        querySuccess = 1

    if c == "path --edit":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "edit")
        else:
            print("Error: path does not exist")
        querySuccess = 1

    if c == "path --properties":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "properties")
        else:
            print("Error: path does not exist")
        querySuccess = 1

    if c == "path --find":
        path = input("path: ")
        os.startfile(f"{path}", "find")
        querySuccess = 1

    # always keep at bottom | error msg
    if querySuccess == 0 and not c == "":
        print(f'command: {c} not found')


# init
def clockSpeed(f):
    while True:
        hertz = 1 / f
        time.sleep(hertz)
        callback()


attempts = 3

user = False
password = False

while attempts > 0:
    password = input("Password: ")
    user = input("User: ")

    if password == "admin":
        password = True

    if user == "admin":
        user = True

    if user == True and password == True:
        print("Logging you in...")
        os.system('cls' if os.name == 'nt' else 'clear')
        clockSpeed(50)

    else:
        attempts -= 1
        print(f'Wrong details, {attempts} attempts left')
