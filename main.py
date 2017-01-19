from PIL import Image, ImageGrab
from datetime import datetime, date, time
import sched, time
import os

os.makedirs('./screen')

s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    dt = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    img = ImageGrab.grab()
    img.save('./screen/' + dt +".png", "PNG")
    s.enter(10, 1, do_something, (sc,))

s.enter(10, 1, do_something, (s,))
s.run()