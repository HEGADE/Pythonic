from plyer import notification

def encode():
    a=""
    print("you need to remember simple words, and we will convert into strong password..\n")
    while(True):
        passstr=input("enter password  ,pls do not include special symbols and number\n").lower()

        if(len(passstr)<4):
            print("password must be longer than 4 words\n")

        else:
            result=""
            securedpat={         "a":"ac1:","b":"&c1","c":"&+s1","d":"$","e":"$+1","f":"%q","g":"s&o8-li*d",
            "h":"2hig","i":"!","j":"~!","k":"12","l":"knight","m":"67","n":"g:4e","o":"0","p":"*`","q":"^as",
            "r":"32:c33","s":"43e","t":"?:","u":"!:@","v":"as33","w":"44#","x":"xf","y":"zo","z":"cip4#3her"}
            for i in passstr:
                for key,value in securedpat.items():
                    if(i in key):
                        re=i.replace(i,value)
                        result=result+re
                        a=result.replace(i,"")
                    
                    

            print("your's secured password is",end="    "+a)
            notification.notify(
                title="Password  Is Genatared",
                message=f"your's secured password is { a}",
                timeout=10
            )
            break    
    
if __name__ == "__main__":
    encode()

