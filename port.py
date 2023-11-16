from serial.tools.list_ports import comports
from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

for port, desc, hwid in sorted(comports()):
    print("%s" % (port))

