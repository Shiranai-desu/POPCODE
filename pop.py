import time,random

while True:
    random.seed(int(time.time()))
    try:
        time.sleep(random.randint(0,10)/100)
        0/0
    except Exception as oiiai:
        print(f"{random.randint(0,1000000)}hello world {oiiai}:  {oiiai}")
