import time
from playsound import playsound

def timer(minute):
    playsound("soundfiles/Start.wav")
    for min in range(minute - 1, -1, -1):
        for sec in range(59, -1, -1):
            if min == 5 and sec == 0:
                playsound("soundfiles/Break.wav")
                print("Rest time")
            if min == 0 and sec == 0:
                playsound("soundfiles/Finish.wav")
                print("time's up!")
            if sec < 10:
                sec = f"0{sec}"
            print(f"{min}:{sec}",end="\r")
            time.sleep(1)


print(open("textfiles/intro.txt", 'r').read())
print(open("textfiles/durnations.txt", 'r').read())

user_input = int(input("Choose your Durnation: "))

if user_input == 1:
    print("Your 30-minute Pomodoro session has begun:")
    timer(30)
elif user_input == 2:
    print("Your 60-minute Pomodoro session has begun:")
    timer(60)
elif user_input == 3:
    print("Your 90-minute Pomodoro session has begun:")
    timer(90)
elif user_input == 4:
    print("Your 120-minute Pomodoro session has begun:")
    timer(120)
elif user_input == 5:
    print("Your 150-minute Pomodoro session has begun:")
    timer(150)
elif user_input == 6:
    print("Your 180-minute Pomodoro session has begun:")
    timer(180)