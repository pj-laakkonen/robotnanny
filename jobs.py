from omaelisa import mobile_blocks
import helpers
import time


def set_blocks(contract, bedtime):
    waiting_time = 30
    tries = 5
    i = 0
    start_time = time.time()
    while i < tries:
        print(helpers.timestamp())
        try:
            mobile_blocks(contract, bedtime)
            print("Succeeded")
            print("---------------------------------")
            break
        except:
            print("Failure, try again!")
            print("Wait " + waiting_time + " seconds...")
            print("---------------------------------")
            time.sleep(waiting_time)
        i += 1

    end_time = time.time()
    helpers.elapsed_time(start_time, end_time)
