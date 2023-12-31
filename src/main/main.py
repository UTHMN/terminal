import time
import socket
import getpass
import sys
import os
import turtle
import pyperclip
import json
import cowsay
import requests
from git import Repo

import fileviewer
import benchmark
import webviewer
import fileeditor
import youtubedownloader

global iNav
global querySuccess
global sString
iNav: bool = False
querySuccess: bool = False

# def
def callback():
    # init
    querySuccess = False
    c = input(getpass.getuser() + "@" + socket.gethostname() + ": ")

    # cmds
    # easter eggs

    # SHIBE
    if c == "shibe":
        url = "http://shibe.online/api/shibes"
        r = requests.get(url)
        rContent = r.content
        print(rContent)
        querySuccess = True

    # CAT

    elif c == "cat":
        url = "http://shibe.online/api/cats"
        r = requests.get(url)
        rContent = r.content
        print(rContent)
        querySuccess = True

    # BIRD

    elif c == "bird":
        url = "http://shibe.online/api/birds"
        r = requests.get(url)
        rContent = r.content
        print(rContent)
        querySuccess = True

    # circle :O

    elif c == "circle :0":
        turtle.circle(50)
        querySuccess = True
        turtle.exitonclick()
        print("DO NOT REOPEN")

    # rectangle :[]

    elif c == "square :[]":
        turtle.shape("square")
        turtle.exitonclick()
        querySuccess = True
        print("DO NOT REOPEN")

    # main cmds

    # print command

    elif c == "print":
        i = input("query: ")
        print(i)
        querySuccess = True

    # exit terminal

    elif c == "exit" or c == "quit":
        querySuccess = True
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()

    # benchmarking tool

    elif c == "benchmark":
        benchmark.init()
        querySuccess = True

    # cmds list

    elif c == "help":
        print("STANDALONE COMMANDS:")
        print("help                 Displays list of commands")
        print("exit                 Exits the terminal")
        print("print                Prints the given query")
        print("Clear                Clear the terminal")
        print("GIT TOOLSET:")
        print("git --init           Initialize a git repository")
        print("APPLICATIONS:")
        print("fileviewer           Opens a given file in terminal and is faster than webviewer")
        print("webviewer            Opens a given file in default webbrowser and is higher resolution than fileviewer")
        print("benchmark            Simple benchmark in terminal, enter to retest")
        print("fileeditor           Simple GUI file editor")
        print("ytdownoader          Youtube video downloader")
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
        print("git --clone          Clones given repository into given path")
        querySuccess = True

    # Apps
        
    # Youtubedownloader
        
    elif c == "ytdownloader":
        #TODO: add ability to choose to either download audio + video, audio or video
        youtubedownloader.Download()
        querySuccess = True
        
    # Fileeditor
        
    elif c == "fileeditor":
        querySuccess = True
        TextEdit = fileeditor.TextEdit()

    # Fileviewer

    elif c == "fileviewer":
        fileviewer.init()
        querySuccess = True

    # Webviewer

    elif c == "webviewer":
        webviewer.init()
        querySuccess = True

    # settings
    
    elif c == "settings":
            if os.path.exists("tSettings.json"):
                os.remove("tSettings.json")
            param1 = input("param1: ")
            param2 = input("param2: ")
            sDict = {"p1": param1, "p2": param2}
            jsonString = json.dumps(sDict)
            jsonFile = open("tSettings.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            print("Changes require a restart to take effect, restart now?")
            tMode = input("Answer: ")
            if tMode == "Yes" or tMode == "yes":
                sys.exit()
            querySuccess = True

    # clear terminal

    elif c == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        querySuccess = True

    # git toolset
        
    elif c == "git --init":
        mode = input("New Repo or Existing Repo: ")
        if mode == "New Repo":
            path_to_dir = input("path to dir: ")
            repo = Repo.init(f"{path_to_dir}")
        elif mode == "Existing Repo":
            path_to_dir = input("path to dir: ")
            repo = Repo(path_to_dir)

    elif c == "git --clone":
        try:
            repo_url = input("link to repo: ")
            path_to_dir = input("where to clone: ")

            if path_to_dir.endswith("/"):
                repo_name = input("Name of repository: ")
                new_path = path_to_dir + (f"{repo_name}")
                os.makedirs(f"{new_path}")
            elif not path_to_dir.endswith("/"):
                repo_name = input("Name of repository: ")
                new_path = path_to_dir + (f"/{repo_name}")
                os.makedirs(f"{new_path}")

            repo = Repo.clone_from(repo_url, new_path)
            print("Success!")

        except Exception as error:
            print(f"error: {error}")

        querySuccess = True

    # path toolset

    elif c == "path --read":
        f = open(f"{input('file: ')}", 'r')
        file_contents = f.read()
        print("=====================")
        print(file_contents)
        input("press {enter} to close")
        f.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        querySuccess = True

    elif c == "path --nav":
        tPath = input("directory to start searching: ") + "/"
        print(os.listdir(f"{tPath}"))
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
        querySuccess = True

    elif c == "path --size":
        pathSize = input("Directory path to be read: ")
        if os.path.exists(f"{pathSize}"):
            peth = os.path.getsize(f'{pathSize}') / 100
            print(f'{pathSize} is {peth} gigabytes')
        else:
            print("Error: path does not exist")
        querySuccess = True

    elif c == "path --current":
        if os.path.exists(f"{os.getcwd()}"):
            print(f'Current directory: {os.getcwd()}')
        else:
            print("Error: file does not exist")
        querySuccess = True

    elif c == "path --add":
        pathAdd = input("Directory path to be created: ")
        os.makedirs(f"{pathAdd}")
        querySuccess = True

    elif c == "path --list":
        pathList = input("Directory path to be listed: ")
        if os.path.exists(f"{pathList}"):
            print(os.listdir(f"{pathList}"))
        else:
            print("Error: file does not exist")
        querySuccess = True

    elif c == "path --remove":
        pathRemove = input("Directory path to be removed: ")
        if os.path.exists(f"{pathRemove}"):
            os.remove(f"{pathRemove}")
        else:
            print("Error: directory does not exist")
        querySuccess = True

    elif c == "path --open":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "open")
        else:
            print("Error: file does not exist")
        querySuccess = True

    elif c == "path --print":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "print")
        else:
            print("Error: file does not exist")
        querySuccess = True

    elif c == "path --edit":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "edit")
        else:
            print("Error: path does not exist")
        querySuccess = True

    elif c == "path --properties":
        path = input("path: ")
        if os.path.exists(f"{path}"):
            os.startfile(f"{path}", "properties")
        else:
            print("Error: path does not exist")
        querySuccess = True

    elif c == "path --find":
        path = input("path: ")
        os.startfile(f"{path}", "find")
        querySuccess = True

    # always keep at bottom | error msg
    if not querySuccess and not c == "":
        print(f"command: {c} not found")


# init
def __init__(f):
    if os.path.exists("./tSettings.json"):
        tSet = open("tSettings.json")
        tSettings = tSet.read()
        sString = json.dumps(tSettings)
        print(f"Successfully Managed to import tSettings.json with data: {sString}, continuing with setup")
    else:
        print("Failed to get tSettings.json, continuing with setup")

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

__init__(50)  # REMOVE ONCE PASSWORD SYSTEM IS RE-ADDED
