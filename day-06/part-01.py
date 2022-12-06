with open("input.txt", "r") as file:
    stream = file.read()
    for i in range(3, len(stream)):
        interval = stream[i-3:i+1]
        if len(interval) == len(set(interval)):
            print(i+1)
            break
