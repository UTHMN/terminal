import os

def removefile(file):
    try:
        if os.path.exists(f"{file}"):
            os.remove(f"{file}")
            print(f"Successfully removed: {file}")
        else:
            print("error file does not exist")
            print(f"error: file: {file} does not exist")
    except:
        print("an error has occured")

def removebatch(file_list):
    for i in range(len(file_list)):
        try:
            if os.path.exists(f"{file_list[i]}"):
                os.remove(f"{file_list[i]}")
                print(f"Successfully removed: {file_list[i]}")
            else:
                print(f"error: file: {file_list[i]} does not exist")
        except:
            print("an error has occured")