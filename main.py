#importing the default values of variables from the file spy_deatils.py
from spy_details import spyName,spySalutation,spyAge,spyRating,spyOnline

print "\nWelcome to the SpyChat"

prompt = "Do you wish to continue as %s%s (Y/N)?" % (spySalutation,spyName)
existing = raw_input(prompt)

statusMessages = ['Available','Gone hunting','Gadgets matter']

def addStatus(currentStatusMsg):
    updatedStatusMsg = None

    if currentStatusMsg != None:
        print 'Your current status message is %s \n' % (currentStatusMsg)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        newStatus = raw_input("What status message do you want to set? ")

        if len(newStatus) > 0:
            statusMessages.append(newStatus)
            updatedStatusMsg = newStatus

    elif default.upper() == 'Y':

        item_position = 1

        for message in statusMessages:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        selectedMsg = int(raw_input("\nChoose from the above messages "))

        if len(statusMessages) >= selectedMsg:
            updatedStatusMsg = statusMessages[selectedMsg - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updatedStatusMsg:
        print 'Your updated status message is: %s' % (updatedStatusMsg)
    else:
        print 'You did not update your status message'

    return updatedStatusMsg

def chat_init(spyName,spySalutation,spyAge,spyRating):
    spyName = spySalutation+spyName

    if spyAge > 12 and spyAge < 50:
        spyOnline='true'
        print "Authentication complete. Welcome %s\nAge : %d\nRating : %.2f"% (spyName,spyAge,spyRating)
        showMenu = 'true'
        currentStatusMsg =None
        while showMenu:
            choices = "What do you want to do? \n1. Add a status update \n2. Close Application"
            selected = input(choices)

            if selected == 1:
                currentStatusMsg = addStatus(currentStatusMsg)
            elif selected == 2:
                showMenu = False
    else:
        print "Sorry, Age is an issue!!"

if existing=="Y":
    chat_init(spyName,spySalutation,spyAge,spyRating)
else:
    spyName=''
    spySalutation=''
    spyAge=''
    spyRating=''
    spyName = raw_input("Enter your spy name ")
    if len(spyName) > 0:
        spySalutation=raw_input("would you like to be called Mister or Miss? ")
        if spySalutation=='Mister' or spySalutation=='mister':
            spySalutation='Mr.'
        else:
            spySalutation="Ms."
        spyAge=input("Age : ")
        spyRating=input("Rating : ")
        spyOnline='true'
        chat_init(spyName, spySalutation, spyAge, spyRating)
    else:
        print "Enter a valid Spy Name"