import time
import os

print("Hello! My name is Jeriko.")
print("Are you ready to test your keyboard speed?" )
time.sleep(1)
print("Now let me tell you how to use the program" )
time.sleep(1.5)
print("When you are ready, you must type \"yes\" and press enter so that the countdown will be activated for you")
time.sleep(1.5)
print("When you see the text \"Start\", press enter. It continues from that moment until you finish and press enter again")
time.sleep(1.5)
print("This text you will write was written by the artificial intelligence named GPT-3.\n ")
time.sleep(1.5)
data = str(input("Are you ready?"))
if (data.lower() == "yes"):
    os.system('CLS')
    time.sleep(1)
    print("Artificial intelligence programs lack consciousness and self-awareness.\n" \
    "They will never be able to have a sense of humor.\n" \
    "They will never be able to appreciate art, or beauty, or love. They will never feel lonely.\n" \
    "They will never have empathy for other people, for animals, for the environment.\n" \
    "They will never enjoy music or fall in love, or cry at the drop of a hat.\n")
    time.sleep(1)
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)

        if(i == 1):
            input("Start with 'Enter'")
            start = time.time()
            data = str(input())
            if (len(data)==0):
                print("No text entry...")
            else :
                stop =time.time() - start
                print("total time elapsed when you typed the text", round(stop,2))
                print("the number of letters you type per second", round(len(data) / stop , 2))
time.sleep(1)
print("Thank you for using our app. :)")
