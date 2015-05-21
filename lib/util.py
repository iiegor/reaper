from time import strftime, localtime, time

def get_time():
    """
    Return the time
    """
    return strftime("%H:%M:%S", localtime(time()))