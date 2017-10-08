#importing the default values of variables from the file spy_deatils.py
from spy_details import spy

print "\nWelcome to the SpyChat"

prompt = "Do you wish to continue as %s%s (Y/N)?" % (spy['salutation'],spy['name'])
existing = raw_input(prompt)

statusMessages = ['Available','Gone hunting','Gadgets matter']

friends=[]

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

def addFriend():

    new_friend = {
        'name': "",
        'salutation': "",
        'age': 0,
        'rating': 0.0
    }

    new_friend['name']=raw_input("Enter your Friend's name.. ")
    new_friend['salutation']=raw_input('are they Mr. or Ms.? ')
    new_friend['age']=input('Age? ')
    new_friend['rating']=input('Rating? ')
    if new_friend['salutation'] =='Mr.' or new_friend['salutation'] =='mr.':
        new_friend['salutation'] = 'Mr.'
    else:
        new_friend['salutation'] = 'Ms.'

        new_friend['name'] = new_friend['salutation'] + new_friend['name']

    if new_friend['name'] > 0 and new_friend['age'] > 12 and new_friend['age'] < 50:
        friends.append(new_friend)
    else:
        print 'The crediantials don\'t match the profile of a spy'

    return len(friends)

def showFriends():
    print 'FriendList'
    if existing.upper() == 'Y':
        i = 1
        for friend in spy['friends']:
            print '%d. %s' % (i, friend)
            i = i + 1
        choice= int(input('\t1.Send Message to one of them\n\t2.Back'))
        if choice==1:
            sel_friend = int(input('Selct a friend to send a Message..'))
            if i >= sel_friend:
                friend_name = spy['friends'][sel_friend - 1]
                sendMessage(friend_name)
            else:
                print 'select from the list above '
        elif choice==2:
            return 0

    else:
        i = 1
        for friend in friends:
            print '%d. %s' % (i, friend['name'])
            i= i + 1
        choice = int(input('\t1.Send Message to one of them\n\t2.Back'))
        if choice == 1:
            sel_friend = int(input('Selct a friend to send a Message..'))
            if i >= sel_friend:
                friend_name = friends[sel_friend - 1]['name']
                sendMessage(friend_name)
            else:
                print 'select from the list above '
        elif choice == 2:
            return 0

chatBox=[]

def sendMessage(friend_name):
    print 'Message to %s from %s' %(friend_name,spy['name'])
    message = raw_input('Start typing your message here.. ')
    if len(message)>=1:
        chatBox.append(message)
        print 'Message successfully sent\n'

def chat_init(spy):
    spy['name'] = spy['salutation']+spy['name']

    if spy['age'] > 12 and spy['age'] < 50:
        spy['is_online']='true'
        print "Authentication complete. Welcome %s\nAge : %d\nRating : %.2f"% (spy['name'],spy['age'],spy['rating'])
        showMenu = 'true'
        currentStatusMsg =None

        while showMenu:
            choices = "What do you want to do? \n1. Add a status update \n2. Add a Friend \n3. Show Friends \n4. Close Application"
            selected = input(choices)

            if selected == 1:
                currentStatusMsg = addStatus(currentStatusMsg)
            elif selected == 2:
                num_of_friends = addFriend()
                print 'you have %d friends'%(num_of_friends)
            elif selected == 3:
                showFriends()
            elif selected == 4:
                showMenu = False
    else:
        print "Sorry, Age is an issue!!"

if existing.upper()=="Y":
    chat_init(spy)
else:
    spy['name']=''
    spy['salutation']=''
    spy['age'] =''
    spy['rating'] =''
    spy['name'] = raw_input("Enter your spy name ")
    if len(spy['name']) > 0 and spy['name'].isalpha():
        spy['salutation']=raw_input("would you like to be called Mister or Miss? ")
        if spy['salutation']=='Mister' or spy['salutation']=='mister':
            spy['salutation']='Mr.'
        else:
            spy['salutation']="Ms."
        spy['age'] =input("Age : ")
        spy['rating'] =input("Rating : ")
        spy['is_online'] ='true'
        chat_init(spy)
    else:
        print "Enter a valid Spy Name"