import time

def log(text):
    with open("log.txt", "a") as f:
        print(f"[{time.time()}] : {text}")
        f.write(f"[{time.time()}] : {text}\n")