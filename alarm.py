from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        min_left = time_left // 60
        sec_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{min_left:02d}:{sec_left:02d}")
        
        
    playsound("aaa.mp3")




minutes = int(input("enter how many minutes: "))
seconds = int(input("enter how many seconds: "))
total_Seconds = minutes * 60 + seconds
alarm(total_Seconds)














