import psutil
import os
import time

global MainLoop

def init():
    start_time = time.time()
    MainLoop = True
    while MainLoop:
        fps = (1.0 / (time.time() - start_time)) * 100
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Cpu Usage:                 {psutil.cpu_percent(interval=0)}%")
        print("")
        print(f"Cpu Count:                 {psutil.cpu_count(logical=False)}")
        print("")
        print(f"Disk Usage:                {psutil.disk_usage('/')}")
        print("")
        print(f"Boot Time:                 {psutil.boot_time()}")
        print("")
        print(f"Battery Level:             {psutil.sensors_battery()}")
        print("")
        print("FPS: ", round(fps, 2))
        print("")
        print(f"Operating System:          {os.name}")
        print("")
        print(f"Temperature:               {psutil.sensors_temperatures(False)}")

        if input("") == "exit":
            MainLoop = False
