from win32com.client import Dispatch
from plyer import notification
import datetime
print("set your reminder ")
let=input("format 20-02-20(pm) or 08-02-02(am)\n")
def drinkWaterremainder():
    while True:
        ti=datetime.datetime.now().strftime("%H-%M-%S")
        if(ti==let):
            speak=Dispatch("SAPI.SpVoice")
            notification.notify(title="Drink Water Notification",
            app_name="ninja",
            message="Sir You Need to Take rest, and you should drink some water this is good for your health",
            timeout=10
            )
            speak.speak("I am your Big Fan sir.")
            speak.speak("chatur intelligence is online")
            go="Sir You Need to Take rest,and you should drink some water this is good for your health"
            speak.speak(go)
            break

        
if __name__ == "__main__":
    drinkWaterremainder()