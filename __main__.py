'''
Created on Jun 19, 2023

@author: ender
'''

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

def main():
    while(True):
        print("Alright, master! I'm gonna help you with clicking now.")
        
        print("How many sets of fields am I clicking?")
        numTypeFields = int(input("Number of sets: "))
        berriesToUse = []
        fieldsInSet = []
        
        for x in range(numTypeFields) :
            
            print("What number berry should I be using for the " + str(x) + 
                " set of fields?")
            berriesToUse.append(int(input("Berry to use: ")))
            
            print("Okay- And how many fields are in this set?")
            fieldsInSet.append(int(input("Number of fields in set: ")))
            
        print("How long do you think I'll have to wait between fields?")
        delayToLoad = int(input("Expected Delay (milliseconds): "))
        
        print("Alright master! I'm ready to click- Just hover over where I should" +
            " click, and hit the Enter key- I will start then!")
        
        input("Waiting for Enter...")
        
        keyboard = KeyboardController()
        mouse = MouseController()
        
        
        for x in range(numTypeFields):
            mouse.click(Button.left, 1)
            for y in range(fieldsInSet[x]):
                keyboard.press(str(berriesToUse[x]))
                keyboard.release(str(berriesToUse[x]))
                for z in range(6):
                    mouse.click(Button.left, 1)
                    time.sleep(5/1000)
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                time.sleep(delayToLoad/1000)
        print("Alright! Done!")
    
    
if __name__ == "__main__":
    main()