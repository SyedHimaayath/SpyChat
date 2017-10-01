#importing the default values of variables from the file spy_deatils.py
from spy_details import spyName,spySalutation,spyAge,spyRating,spyOnline

print "\nWelcome to the SpyChat"

prompt = "Do you wish to continue as %s%s (Y/N)?" % (spySalutation,spyName)
existing = raw_input(prompt)

def chat_init(spyName,spySalutation,spyAge,spyRating,spyOnline):
    spyName = spySalutation+spyName

    if spyAge > 12 and spyAge < 50:
        spyOnline='true'
        print "Authentication complete. Welcome %s\nAge : %d\nRating : %.2f"% (spyName,spyAge,spyRating)

if existing=="Y":
    chat_init(spyName,spySalutation,spyAge,spyRating,spyOnline)
else:
    spyName=''
    spySalutation=''
    spyAge=''
    spyRating=''

    spyName=raw_input("Enter your spy name ")
    spySalutation=raw_input("would you like to be called Mister or Miss? ")
    if spySalutation=='Mister':
        spySalutation='Mr.'
    else:
        spySalutation="Ms."
    spyAge=input("Age : ")
    spyRating=input("Rating : ")
    chat_init(spyName, spySalutation, spyAge, spyRating, spyOnline)