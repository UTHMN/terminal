def debug_mode(self):
        try:
            inp = input("$~")
            exec(inp)

        except Exception as error:
            print(error)

while True:    
    debug_mode("")