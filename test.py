import time
seconds = time.time()
print(seconds)
time.sleep(2)
print(time.time() - seconds)
while True:
    input("Hi: ")
    if int(time.time() - seconds) >= 20:
        print('Ok')
        seconds = time.time()
    else:
        print(f'Wait for 20 Second: {int(time.time() - seconds)}')
        continue
    print(int(time.time() - seconds))