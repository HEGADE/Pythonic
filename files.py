import os
from plyer import notification
from win32com.client import Dispatch
files=os.listdir(r'C:\Users\SUBRAHMANYA\Documents\lpashare\lapshare\media')

temp=len(files)

while True:
    speak=Dispatch("SAPI.SpVoice")
    files=os.listdir(r'C:\Users\SUBRAHMANYA\Documents\lpashare\lapshare\media')
    tlen=len(files)
    

        
    if temp<tlen:
        sir=f'sir we have received file successfully'
        print('is greatest')
        temp=len(files)
        notification.notify(title="Received successfully",
                app_name="ninja",
                message=sir,
                timeout=10
                )
        go=sir
        speak.speak(go)
    elif temp>tlen:
        temp=len(files)
        print('kammi ede')
    
    else:
        pass

