#Spencer Goldwin
#Trouble Shooting WIFI Connectivity

print("Reboot the computer and try to connect.")
answer = input("Did that fix the problem? ")

if answer =='no':
    print("Renoot the router and try to connect.")
    answer = input("Did that fix the problem? ")
    if answer == 'no':
        print("Make sure the cables between the router & modem are plugged in firmly.")
        answer = input("Did that fix the problem?")
        if answer == 'no':
            print("Move the router to a new location and try to connect.")
            answer = input("Did that fix the problem? ")
            if answer == 'no':
                print("Get a new router.")
    
else:
    print("Congratulations you are connected.")
