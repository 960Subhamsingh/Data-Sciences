"""
5. Lets say you are running a 50 km race. Write a program that, 

*   Upon completing each 10 km asks you "are you tired?" 
*   If you reply "yes" then it should break and print "you didn't
finish the race"
*   If you reply "no" then it should continue and ask "are you tired" on every km
*   If you finish all 50 km then it should print congratulations message

"""

for dis in range(50):
       if (dis<50 and dis%10==0):
        print("are you tired")
        reply = str(input(" Yes/No : "))
        if(reply=="Yes"):
            print("You didn't Finish The Race")
            break
        elif(reply=="No"):
                continue
        else:
             print("Invalid") 
   
print("congratulations")


