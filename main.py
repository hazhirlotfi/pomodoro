import time
from playsound import playsound

def timer(minute):
    pomodoro = int(minute / 30)
    playsound("soundfiles/Start.wav")

    for _ in range(minute):

        for mins_left in range(minute - 1, -1, -1):
            
            for secs_left in range(59, -1, -1):
                
                if mins_left == 5 and secs_left == 0:
                    playsound("soundfiles/Break.wav")
                    print("Rest time")

                if mins_left == 0 and secs_left == 0:
                    playsound("soundfiles/Finish.wav")
                    print("Time's up!")
                    return

                print(f"{mins_left:02}:{secs_left:02}", end = "\r") 
                time.sleep(1)
                
print(open("textfiles/intro.txt", 'r').read())
print(open("textfiles/durations.txt", 'r').read())




while True:
    
    try:
        user_input = int(input("Choose your duration: "))

        pomos = {
            1 : 30,
            2 : 60, 
            3 : 90,
            4 : 120,
            5 : 150,
            6 : 180
            }
        
        if user_input in pomos.keys():
            print(f"Your {pomos[user_input]} minutes duration has begun.")
            timer(pomos[user_input])
        else:
            print("come on man! it's simple. Choose a number from 1 to 6.")
    except ValueError:
        print("WOW! you went for something other than numbers? choose 1 or 2 or 3 or 4 or 5 or 6. Okay?")



