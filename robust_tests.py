from wakeup import wakeup
from gotosleep import gotosleep
import helpers
import time

bedtime = True
n = 10

waiting_time = 30
pause_time = 5

start_time = time.time()

for i in range(n):
    print("Test: " + str(i+1) + "/" + str(n))
    if i % 2 == 0:
        print("wakeup")
        wakeup()
    else:
        print("gotosleep")
        gotosleep()

    time.sleep(pause_time)

end_time = time.time()-pause_time
print("---------------------------------")
print("Number of tests:" + str(n))
helpers.elapsed_time(start_time, end_time)
