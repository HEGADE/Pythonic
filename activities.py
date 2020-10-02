
"""This is the degital wellbeing prg that helps to identify time spent for each app in the system,but it won't identify the visual studio code because some security purpose"""
"""author is S Hegade"""
__version__="1.0.0"

from win32gui import GetWindowText,GetForegroundWindow,GetWindow
import datetime
from plyer import battery,notification
from  time import sleep

def degital():
    """the function for calcultion and identification of the  which is currently opened window and its time"""
    infoObj={}
    closedObj={}
    openedWindowObj={}
    WindowOTime=""
    WindowCTime=""
    
    def openedTime():
        #function for finding opened time
        global WindowOTime
        WindowOTime=datetime.datetime.now().strftime("%H-%M-%S")
        return WindowOTime

    def closedTime():
        # function for finding closed time
        global WindowCTime
        WindowCTime=datetime.datetime.now().strftime("%H-%M-%S")
        return WindowCTime

    try:
        while True:
            #actual process starts here....
            openedWindow=GetWindowText(GetForegroundWindow())
            currentWindow=openedWindow.split("-")[-1]
            if GetForegroundWindow():
                if currentWindow not in infoObj:
                    print("true")
                    oo=openedTime()
                    infoObj[currentWindow]=oo
                    openedWindowObj[currentWindow]=oo
                    blood=[currentWindow]
                
                else:
                    pass

                if currentWindow!=blood[0]:
                    clo=closedTime()
                    closedObj[blood[0]]=clo                
                
                else:
                    pass


    except KeyboardInterrupt as e:
        if "" in openedWindowObj:
            openedWindowObj.pop('')
        if ' Visual Studio Code' in openedWindowObj:
            del openedWindowObj[' Visual Studio Code']
        for key,value in openedWindowObj.items():
            totaltime=value.split("-")
            a=int(totaltime[0])
            b=int(totaltime[1])
            c=int(totaltime[2])
            for kk,vv in closedObj.items():
                totaltime1=vv.split("-")
                a2=int(totaltime1[0])
                b2=int(totaltime1[1])
                c2=int(totaltime1[2])
                x=str(a-a2)
                y=str(b-b2)
                z=str(c-c2)
                z1=x.replace("-","")
                z2=y.replace("-","")
                z3=z.replace("-","")
            print(f"you used { key}  for  { z1}Hours  {z2}Minutes and { z3}seconds")

            if int(z1)>=1:
                notification.notify(
                    title="Time to take Rest",
                    message=f"you are using {key} from   { z1}Hours   {z2}Minutes  and   { z3}seconds pls take rest",
                    timeout=8
                )
        
        batt=battery.status
        for keyB,valueB in batt.items():
            print(
                keyB,valueB
            )

if __name__ == "__main__":
    degital()
