with open("input.txt", "r") as file:
    stream = file.read()
    for i in range(13, len(stream)):
        interval = stream[i-13:i+1]
        if len(interval) == len(set(interval)):
            print(i+1)
            break