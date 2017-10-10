#importing the default values of variables from the file spy_deatils.py
from spy_details import Spy, Chat
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import cprint
import csv
from colorama import Fore, Back
import sys

spy = Spy('Johnny English', 'Mr.', 33, 5)

print "\nWelcome to the SpyChat"
prompt = "Do you wish to continue as %s%s (Y/N)?" % (spy.salutation,spy.name)
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

    # new_friend['name']=raw_input("Enter your Friend's name.. ")
    # new_friend['salutation']=raw_input('are they Mr. or Ms.? ')
    # new_friend['age']=input('Age? ')
    # new_friend['rating']=input('Rating? ')

    newspy = Spy(raw_input("Please enter your friend's name:"), raw_input("Are they Mr. or Ms.?: "),
                 input("What's the age?"), input("What is their Spy rating?"))

    if newspy.salutation =='Mr.' or newspy.salutation =='mr.':
        newspy.salutation = 'Mr.'
    else:
        newspy.salutation = 'Ms.'

        newspy.name = newspy.salutation + newspy.name

    if len(newspy.name) > 0 and newspy.age > 12 and newspy.age < 50:
        friends.append(newspy)
        with open("friends.csv.txt", "a") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([newspy.name, newspy.salutation, newspy.age, newspy.rating, True])
        print "Friend Added !!"
    else:
        print 'The crediantials don\'t match the profile of a spy'

    return len(friends)

def select_friend():

    i = 1
    for friend in friends:
        print '%d. %s' % (i, friend.name)
        i = i + 1
    selected_one = input('Select a friend from the list above')
    selected_friend = selected_one - 1
    return selected_friend


def sendMessage():
    friend_selected = select_friend()
    if friend_selected >=0:
        original_image = raw_input("What is the name of the image?")
        output_path = 'output.jpeg'
        text = raw_input("What do you want to say?")
        Steganography.encode(original_image, output_path, text)

        new_chat = Chat(text, spy.name)

        friends[friend_selected].chats.append(new_chat)
        with open('chats.csv.txt','a') as chat_box:
            sender = csv.writer(chat_box)
            sender.writerow([friends[friend_selected].name, new_chat.message, new_chat.sent_by, new_chat.time ])
        print "Your secret message image is ready!"
    else:
        print 'You seem to have no friends'

def readMessage():
    sender=select_friend()
    input_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(input_path)
    new_chat = Chat(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

def loadFriends():
    with open("friends.csv.txt", "rb") as friends_list:
        reader = list(csv.reader(friends_list))

        for row in reader[1:]:
            spy1 = Spy(row[0],row[1],row[2],row[3])
            friends.append(spy1)

def loadMessage():
    with open("chats.csv.txt", "rb") as chat_box:
        reader = list(csv.reader(chat_box))

        for row in reader[1:]:
            chatDetails = Chat(row[1],row[2])
            spy.chats.append(chatDetails)

def readChats():
    i=1
    for chat in spy.chats:
        cprint(chat.sent_by,'red')
        print (Fore.BLACK + chat.message)
        cprint(chat.time,'blue')
        i=i+1

def chat_init( spy_name,spy_salutation,spy_age,spy_rating):

    showMenu = 'true'
    currentStatusMsg =None
    loadFriends()
    loadMessage()

    while showMenu:
        choices = "What do you want to do? \n1. Add a status update \n2. Add a Friend \n3. Send Messages " \
                  "\n4. Read Messages \n5. Read Chats \n6. Close Application"
        selected = input(choices)

        if selected == 1:
            currentStatusMsg = addStatus(currentStatusMsg)
        elif selected == 2:
            num_of_friends = addFriend()
            print 'you have %d friends'%(num_of_friends)
        elif selected == 3:
            sendMessage()
        elif selected ==4:
            readMessage()
        elif selected ==5:
            readChats()
        elif selected == 6:
            showMenu = False
        else:
            sys.exit()

if existing.upper()=="Y":
    chat_init(spy.name,spy.salutation,spy.age,spy.rating)
else:
    spy.name=''
    spy.salutation=''
    spy.age=0
    spy.rating=0.0
    spy.name = raw_input("Enter your spy name ")
    if len(spy.name) > 0 and spy.name.isalpha() == True:
        spy.salutation =raw_input("would you like to be called Mister or Miss? ")
        if spy.salutation =='Mister' or spy.salutation =='mister' or spy.salutation == 'Mr.' or spy.salutation =='mr.':
            spy.salutation='Mr.'
        else:
            spy.salutation="Ms."
        spy.age =input("Age : ")
        spy.rating =input("Rating : ")
        if spy.age > 12 and spy.age < 50:
            print "Authentication complete. Welcome %s%s\nAge : %d\nRating : %.2f" % (spy.salutation,spy.name, spy.age, spy.rating)
            chat_init(spy.name,spy.salutation,spy.age,spy.rating)
    else:
        print "Enter a valid Spy Name"