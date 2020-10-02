import os
from pathlib import Path
from sys import path
from plyer import notification


def antiV():   
        homepath=Path.home()
        path=f'{homepath}\\documents'
        st=r"del %sytemdrive%"
        o=os.walk(path,followlinks=True)
        dirr=os.listdir(path)
        for i in o:
                for i1 in i[2]:
                        i0=os.path.join(i[0], i1)
                        f=open(i0,"br")
                        a=f.read()
                        f.close()
                        if st in str(a):
                                if r"C:\Users\SUBRAHMANYA\documents\PRG"==i[0]:
                                        pass
                                else:
                                        notification.notify(
                                                title="Virus Protection",
                                                message="we have found some virus",
                                                timeout=10
                                        )
                                        os.remove(i0)


if __name__ == "__main__":
    antiV()
