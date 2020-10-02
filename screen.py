from plyer import screenshot
from plyer import battery
from PIL import Image
from time import sleep
# screenshot.file_path=r"C:\Users\GFGC\Documents\PRG\sc.png";
# screenshot.capture()
a=battery.status
while(1):
    for key,value in a.items():
        print(key+":",value)
    sleep(10)
    