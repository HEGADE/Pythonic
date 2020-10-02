"""Cipher
------------------------------
the god mode  is enabled
what are you looking for
this is the game for beginers
the game module by s Hegade
------------------------------
"""
import random
def luck():
    """this is the prg which takes the number as out_put and matches among the random numbers, 
       if the input matches then it returns true"""
    print("game started..")
    print("lets check your luck..")
    chance=0
    while(True):
        entry=int(input("enter the number between 0 and 10\n"))
        ran=random.randint(0,10)
        if(entry==ran):
            print("you won the game ,So your  lucky, have a good day👍👍")
            break
        else:
            chance=chance+1
            print("try again")
            if(chance>3):
                print(" better luck next time😊😊😊")   
                break

if __name__ == "__main__":
    luck()

