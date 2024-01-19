import os

def pymrk_initialize(self):
    if os.path.exists("PyMrk") and os.path.exists("PyMrk/Dict") and os.path.exists("PyMrk/Snippets"):
        pass
    else:
        cwd = os.getcwd()
        path = os.path.join(cwd, "PyMrk/Dict")
        os.makedirs(f"{path}")
        path = os.path.join(cwd, "PyMrk/Snippets")
        os.makedirs(f"{path}")