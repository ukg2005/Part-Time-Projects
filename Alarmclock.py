import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    sound_file = "../oops/Going Home - The Soundlings.mp3"
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Time is up")
            pygame.mixer.init()
            pygame.mixer.Sound(sound_file).play()
            time.sleep(1)
            choice = input("Press y to stop").lower()
            if choice == "y":
                exit(1)
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time:")
    set_alarm(alarm_time)