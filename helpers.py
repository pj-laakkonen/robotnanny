import datetime


def timestamp():
    now = datetime.datetime.now()
    return now.strftime("%d.%m.%Y %H:%M:%S")


def elapsed_time(start_time, end_time):
    seconds = end_time - start_time
    minutes = seconds // 60
    seconds %= 60
    print("Elapsed time: {0:.0f} minutes {1:.0f} seconds".format(minutes, seconds))
