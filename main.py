import time
import socket
import getpass
import sys
import os
import winsound as ws
import turtle
import pyperclip
import json
import requests

global iNav
global querySuccess
iNav: bool = False
querySuccess: bool = False


# def
def callback():
    # init
    start_time = time.time()
    query_Success = False
    c = input(socket.gethostname() + "@" + getpass.getuser() + ": ")

    # cmds
    # easter eggs

    # SHIBE
    if c == "shibe":
        url = "http://shibe.online/api/shibes"
        r = requests.get(url)
        rContent = r.content
        print(rContent)
        query_Success = True

    # CAT

    if c == "cat":
        url = "http://shibe.online/api/cats"
        r = requests.get(url)
        rContent = r.content
        print(rContent)
        query_Success = True

    # BIRD

    if c == "bird":
        url = "http://shibe.online/api/birds"
        r = requests.get(url)
        rContent = r.content
        print(rContent)
        query_Success = True

    # circle :O

    if c == "circle :0":
        turtle.circle(50)
        query_Success = True
        turtle.exitonclick()
        print("DO NOT REOPEN")

    # rectangle :[]

    if c == "square :[]":
        turtle.shape("square")
        turtle.exitonclick()
        query_Success = True
        print("DO NOT REOPEN")

    # main cmds

    # print command

    if c == "print":
        i = input("query: ")
        print(i)
        query_Success = True

    # exit terminal

    if c == "exit" or c == "quit":
        ws.PlaySound("SystemExit", ws.SND_ASYNC)
        query_Success = True
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

    # benchmarking tool

    if c == "benchmark":
        fps = (1.0 / (time.time() - start_time)) * 100
        print("FPS: ", round(fps, 2))
        print(f"Cpu Cores: {os.cpu_count()}")
        print(f"Operating System: {os.name}")
        query_Success = True

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
        print("path --print         Prints a given file (to the printer)")
        print("path --properties    Finds properties of a file")
        print("path --find          Finds if given file exists")
        print("path --remove        Removes a file at a given path")
        print("path --list          Lists the contents of a directory at a given path")
        print("path --add           Adds a file at a given directory")
        print("path --current       Displays the current path you are running")
        print("path --size          Displays the size of a path in megabytes")
        print("path --nav           Lets you navigate to a certain path and copies it to the clipboard")
        print("path --read          Prints the contents of a file (to the terminal)")
        query_Success = True

    # settings

    if c == "settings":
        mReadWrite = input("mode: ")
        # export mode
        if mReadWrite == "export":
            if os.path.exists("tSettings.json"):
                os.remove("tSettings.json")
            param1 = input("param1: ")
            param2 = input("param2: ")
            sDict = {param1: 1, param2: 2}
            jsonString = json.dumps(sDict)
            jsonFile = open("tSettings.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            sys.exit()
        # load settings
        if mReadWrite == "load":
            tSet = open("tSettings.json")
            tSettings = tSet.read()
            sString = json.dumps(tSettings)
            print(sString)
        # remove file
        if mReadWrite == "remove":
            if os.path.exists("tSettings.json"):
                os.remove("tSettings.json")
            else:
                print("ERROR: NO SETTINGS TO REMOVE")
        # raise error on invalid mode
        if not mReadWrite == "export" and not mReadWrite == "remove" and not mReadWrite == "load":
            print("ERROR: INVALID MODE")

        query_Success = True

    # clear terminal

    if c == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        query_Success = True

    # path toolset

    if c == "path --read":
        f = open(f"{input('file: ')}", 'r')
        file_contents = f.read()
        print("=====================")
        print(file_contents)
        input("press {enter} to close")
        f.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        query_Success = True

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
                print("successfully copied to clipboard, remove the 'exit' string")
                iNav = False
            else:
                tPath = temp + Cpath
                print(os.listdir(tPath))
                temp = tPath + "/"
        query_Success = True

    if c == "path --size":
        pathSize = input("Directory path to be read: ")
        if os.path.exists(f"{pathSize}"):
            peth = os.path.getsize(f'{pathSize}') / 100
            print(f'{pathSize} is {peth} gigabytes')
        else:
            print("Error: path does not exist")
        query_Success = True

    if c == "path --current":
        if os.path.exists(f"{os.getcwd()}"):
            print(f'Current directory: {os.getcwd()}')
        else:
            print("Error: file does not exist")
        query_Success = True

    if c == "path --add":
        pathAdd = input("Directory path to be created: ")
        os.makedirs(f"{pathAdd}")
        query_Success = True

    if c == "path --list":
        pathList = input("Directory path to be listed: ")
        if os.path.exists(f"{pathList}"):
            print(os.listdir(f"{pathList}"))
        else:
            print("Error: file does not exist")
        query_Success = True

    if c == "path --remove":
        pathRemove = input("Directory path to be removed: ")
        if os.path.exists(f"{pathRemove}"):
            os.remove(f"{pathRemove}")
        else:
            print("Error: directory does not exist")
        query_Success = True

    if c == "path --open":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "open")
        else:
            print("Error: file does not exist")
        query_Success = True

    if c == "path --print":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "print")
        else:
            print("Error: file does not exist")
        query_Success = True

    if c == "path --edit":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "edit")
        else:
            print("Error: path does not exist")
        query_Success = True

    if c == "path --properties":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "properties")
        else:
            print("Error: path does not exist")
        query_Success = True

    if c == "path --find":
        path = input("path: ")
        os.startfile(f"{path}", "find")
        query_Success = True

    # always keep at bottom | error msg
    if not query_Success and not c == "":
        print(f"command: {c} not found")


# init
def clockSpeed(f):
    while True:
        hertz = 1 / f
        time.sleep(hertz)
        callback()


# RE-ADD THE PASSWORD SYSTEM LATER

# attempts = 3

# user = False
# password = False

# while attempts > 0:
#   password = input("Password: ")
#  user = input("User: ")

#   if password == "admin":
#      password = True

#  if user == "admin":
#       user = True

#   if user == True and password == True:
#       print("Logging you in...")
#       os.system('cls' if os.name == 'nt' else 'clear')
#      clockSpeed(50)

#   else:
#      attempts -= 1
#      print(f'Wrong details, {attempts} attempts left')

clockSpeed(50)  # REMOVE ONCE PASSWORD SYSTEM IS RE-ADDED
