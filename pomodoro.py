import time

def timer(zaman):
    for min in range(zaman - 1, -1, -1):
        for sec in range(59, -1, -1):
            print(f"{min}:{sec}",end="\r")
            time.sleep(1.2)
            if min == 5:
                print("Rest time")
    #TODO: divde times that are more than 30 minutes.
            
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