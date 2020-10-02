"""Chatur The  Electronic Desk_Top Assistant(EDA)
----------------------------------------------------------
info:chatur is the desktop assistant and user friendly,
so  you can handle many task using chatur.some of them are:-
1)password securing.......................................
2)file handling automatically.............................
3)usage tracking...........................................
4)voice command  activated functions........................
5)system security(acts as an antivirus)...................
6)usage alert(from long time working).....................
7)automatic replay for query(limited).....................
these function can be done by Chatur automatically without 
-user interaction
--------------------------------------------------------
"""
#all rights reserved
__version__="1.0.0"
__author__="S Hegade"
__contact__="null"

import speech_recognition as re
r=re.Recognizer()
with re.Microphone() as source:
    print('listening...')
    r.pause_threshold=1
    audio=r.listen(source)
try:
    print('recognizing')
    query=r.recognize_google(audio,language='en-in')
    print(f'usersaid {query}')
except Exception as e:
    print(e)
