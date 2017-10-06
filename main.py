#importing the default values of variables from the file spy_deatils.py
from spy_details import spyName,spySalutation,spyAge,spyRating,spyOnline

print "\nWelcome to the SpyChat"

prompt = "Do you wish to continue as %s%s (Y/N)?" % (spySalutation,spyName)
existing = raw_input(prompt)

statusMessages = ['Available','Gone hunting','Gadgets matter']

friend_name=[]
friend_age=[]
friend_rating=[]
friend_Is_online=[]

def addFriend():
    new_friend_name=raw_input("Enter your Friend's name.. ")
    new_friend_salutation=raw_input('are they Mr. or Ms.? ')
    new_friend_age=input('Age? ')
    new_friend_rating=input('Rating? ')
    if new_friend_salutation =='Mr' or spySalutation=='mr':
        new_friend_salutation = 'Mr.'
    else:
        new_friend_salutation = 'Ms.'

    new_friend_name = new_friend_salutation + new_friend_name

    if new_friend_name > 0 and new_friend_age > 12 and new_friend_age < 50:
        friend_name.append(new_friend_name)
        friend_age.append(new_friend_age)
        friend_rating.append(new_friend_rating)
    else:
        print 'The crediantials don\'t match the profile of a spy'

    return len(friend_name)

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
            choices = "What do you want to do? \n1. Add a status update \n2. Add a Friend \n3. Close Application"
            selected = input(choices)

            if selected == 1:
                currentStatusMsg = addStatus(currentStatusMsg)
            elif selected == 2:
                num_of_friends = addFriend()
                print 'you have %d friends'%(num_of_friends)
            elif selected == 3:
                showMenu = False
    else:
        print "Sorry, Age is an issue!!"

if existing.upper()=="Y":
    chat_init(spyName,spySalutation,spyAge,spyRating)
else:
    spyName=''
    spySalutation=''
    spyAge=''
    spyRating=''
    spyName = raw_input("Enter your spy name ")
    if len(spyName) > 0 and spyName.isalpha():
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