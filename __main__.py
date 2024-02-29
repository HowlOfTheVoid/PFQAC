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
        
        print("Am I clicking through parties, or fields? (Type \"parties\" or \"fields\".")
        
        typeOfClick = input("Click Type: ")
        
        if(typeOfClick == "parties"):
            print("How many pages of players do you want me to click?")
            numOfPages = int(input("Number of pages: "))
            
            print("How many people are on each page?")
            numOfPeople = int(input("Number of people/page: "))
            
            print("How long does it take for your computer to load the next batch?")
            delayToLoad = int(input("Expected Delay (milliseconds): "))
            
            print("Alright master! I'm ready to click- Just hover over where I should" +
                    " click, and hit the Enter key- I will start then!")
            
            input("Wating for Enter...")
        
            keyboard = KeyboardController()
            mouse = MouseController()
            
            for x in range(numOfPages):
                
                ##Overcompensate for chances of error
                for y in range(numOfPeople + 5):
                    
                    for z in range(8):
                        mouse.click(Button.left, 1)
                        time.sleep(5/1000)
                        
                    time.sleep(400/1000)
                    
                time.sleep(delayToLoad/1000)
            
        if(typeOfClick == "fields"):
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
                    for z in range(40):
                        mouse.click(Button.left, 1)
                        time.sleep(5/1000)
                    time.sleep(delayToLoad/1000)
        else:
            print("It seems like you may have entered neither \"parties\" or \"fields\". Maybe try again?")
        print("Alright! Done!")
    
    
if __name__ == "__main__":
    main()