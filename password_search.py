print("enter username")
uname = input()
print("enter password")
pword = input()

file = open("info.txt", "r")
count = 0
for line in file:
    lineArray = line.split(" | ")
    for details in lineArray:
        if count == 0:
            username = details
            count = count+1
        else:
            password = details.strip("\n")
            count = 0
            if uname == username and pword == password:
                success = True
                break
            else:
                success = False
    if success == True:
        break
if success == True:
    print("Login success for",username)
    wait = input()
else:
    print("Invalid details")
    wait = input()