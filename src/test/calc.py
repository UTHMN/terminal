def calc(inp: str):
    if "+" in inp:
        index = inp.find("+")
        leng = len(inp)
        numOneLen = leng - index - 1
        numTwoLen = leng - numOneLen - 1
        print(f"input:     {inp}")
        print(f"numTwoLen: {numTwoLen}")
        print(f"numOneLen: {numOneLen}")
        print(f"index:     {index}")
        print(f"len:       {leng}")
    elif "-" in inp:
        index = inp.find("-")
        leng = len(inp)
        print(f"input: {inp}")
        print(f"index: {index}")
        print(f"len:   {leng}")
    elif "/" in inp:
        index = inp.find("/")
        leng = len(inp)
        print(f"input: {inp}")
        print(f"index: {index}")
        print(f"len:   {leng}")
    elif "*" in inp:
        index = inp.find("x")
        leng = len(inp)
        print(f"input: {inp}")
        print(f"index: {index}")
        print(f"len:   {leng}")

calc("124214+124123")