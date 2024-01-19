import engine
import getpass
import socket

Running = True
instance = engine.Engine()
instance.pymrk_convert()

while Running:
    c = input(getpass.getuser() + "@" + socket.gethostname() + ": ")
    instance.run(c)