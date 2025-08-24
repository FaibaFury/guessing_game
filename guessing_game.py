import time
import os
import sys

attempts=0
print("i have one fav number from 1 to 14 or maybe not!, lets see if you can guess it!")
while True:
    user_input=int(input())
    if user_input==111:
        print("YOU WON! NOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
    else:
        attempts+=1
        if attempts==1:
            print("darn it! try again!")
            print("come on! ")
        elif attempts==2:
            print("come on man!")
        elif attempts==3:
            print("THINK OUTSIDE THE BOX!!! <<------")
        elif attempts==4:
            print("bruh!")
        elif attempts==5:
            print("no way!i thought you were smart!")
        elif attempts==6:
            print("just get out man!")
        elif attempts==7:
            print("YOU ARE TRIGGERING ME!")
        elif attempts==8:
            print("you are not stupid this much!")
        elif attempts==9:
            print("wow, do you even think! oh i must be talking to tree!")
            print("COMMMMEEEEE ONNNNN!")
        elif attempts==10:
            print("see here ------>>>  !!!  think of this as a number!")
            print("YOU CANT MISS THIS ONE! I JUST GAVE YOU A HIIIIIIIINT!!!!!! JUST ONE MORE MISTAKE!")                                        
        elif attempts==11:
            print("JUST ONE MORE TRY LEFT!HAHAHAHAHAHA!!!!!!!!!!")
        else:
            print("GET TF OUT OF MY GAME!")
            time.sleep(2)
            exit()

    
    

