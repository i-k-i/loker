import subprocess
import time

fp = subprocess.Popen("usb-devices", shell=True, stdout=subprocess.PIPE)
fpout = fp.stdout.readlines()

while True:
    
    time.sleep(.01)
    sp = subprocess.Popen("usb-devices", shell=True, stdout=subprocess.PIPE)
    spout = sp.stdout.readlines()
    for i in spout:
        if i not in fpout:
            print i
            fpout.append(i)
            
