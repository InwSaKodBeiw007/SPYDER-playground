import time
textfristDateofBirth = str(input("Enter the message you want >> ")).lower()
allEngiKnow = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ".lower()

Thetext  = ""
for i in textfristDateofBirth:
    ##print(i)
    for y in allEngiKnow:
        if i == y :
            Thetext += y
            print(f"{Thetext.upper()}")
            break
        else:
            print(f"{Thetext.upper()}{y}")
            time.sleep(0.076)