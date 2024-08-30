import time
from playsound import playsound

def timer(minute):
    pomodoro = int(minute / 30)
    playsound("soundfiles/Start.wav")

    for _ in range(pomodoro):
       
        for mins_left in range(30 - 1, -1, -1):
            
            for secs_left in range(59, -1, -1):
                
                if mins_left == 5 and secs_left == 0:
                    playsound("soundfiles/Break.wav")
                    print("Rest time")

                if mins_left == 0 and secs_left == 0:
                    playsound("soundfiles/Finish.wav")
                    print("time's up!")

                if secs_left < 10:
                    secs_left = f"0{secs_left}"
                    
                print(f"{mins_left}:{secs_left}",end="\r")

                time.sleep(1)


print(open("textfiles/intro.txt", 'r').read())
print(open("textfiles/durnations.txt", 'r').read())

user_input = int(input("Choose your Durnation: "))

pomos = {
    1 : 30,
    2 : 60, 
    3 : 90,
    4 : 120,
    5 : 150,
    6 : 180
    }

if user_input in pomos.keys():
    print(f"Your {pomos[user_input]} minutes durnaion has begun.")
    timer(pomos[user_input])
else:
    print("You pressed the wrong key buddy!, CHOOSE AGAIN")