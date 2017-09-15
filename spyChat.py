print "Welcome to the SpyChat"
spyName = raw_input("Enter Name : ")
spySalutation = raw_input("hello "+spyName+ ", would you like to be addressed mister / miss : ")
print "Welcome "+spySalutation+" "+spyName+", Please fill-in the details to activate your super-secret profile"
spyAge = raw_input("Age : ")
spySecretName = raw_input("Enter you super secret name : ")
if spyAge>"25" and spyAge<"50":
    print "valid user"
    spyRating = raw_input("Enter your rating : ")
    if spyRating > 4:
        print "All-star profile"
    elif spyRating < 4 and spyRating >3:
        print "You need to complete your cases on time"
    elif spyRating<3:
        print "you are in danger zone"

    print "\fSpy Profile"
    print "Name : "+spyName
    print "code name : "+spySecretName
    print "Age : "+spyAge
    print "Rating : "+spyRating
else:
    print "In-valid age to join this org"
