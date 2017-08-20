from datetime import datetime

import tts

def what_is_time():
    tts("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'))
