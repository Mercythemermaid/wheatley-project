#Esther Ashby
#Wheatley project



#imports
#this is where i import exernal funtions
import time

#------
#startting up- this is where the robot turns on
# displays a simple "I'm starting up" greetment phrase

print ("I'm starting up.")
time.sleep(1)
#------
#right after the robot starts up, it has to "reset"
# or go back to the pose layed out for him here
# so he can be ready to preform the next action.
#the predefined "reset" pose is a simple forward
# where all things are at a neutral state

print ("I'm resetting things now")
time.sleep(1)
#------
#this is when the robot checks for imput
#or checking for a button to be pressed
#basically this is a waiting stage
#waiting for a button to be pressed
# if no button is pressed, he stays in this stage

while True:
    

    print ("checking for input...")
    button = input('Select a number: ')
#doop

#------
#when a button is pressed
# this is him preforming the action tied to that specific button
#this part also tells the user which speific button was pressed


    print ("imput found")
    print ('button number ' ,button ,' was pressed')
    time.sleep(1)
#-------
#this is where it tells the user to wait a moment
# while the robot is preforming the action

    print ("preforming action now...")
    time.sleep(1)
#-------
#the robot is now asking wheather it should quit or not-
# asking the user a Y/N question
#if the user says yes, it goes down to the next action
#if the user says no, then it goes back
# to the waiting for imput stage
    awnser = input ("should I quit Y/N?")
    if awnser == "Y" or awnser == "y" or awnser == "yes" or awnser == "Yes" or awnser == "YES":
        print ("OK")
        print ("I am really going to quit")
        print ("I mean really")
        break

    else:
        if awnser == "N" or awnser == "n" or awnser == "no" or awnser == "No" or awnser == "NO":
            print ("OK I guess I should not quit...")
            print ("But I am going to anyway but later I will keep going")
        else:
            print ("Um, you did not answer the question")
            #to do: add loop for invalid entry


