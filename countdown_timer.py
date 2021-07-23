"""A module to implement a countdown timer.
"""
import sys
import time

def countdown_timer(seconds_local: int) -> None:
    """A simple function that implements a countdown timer to countdown time
    in seconds.
    """
    print("Starting the countdown timer.")

    for seconds_elapsed in range(seconds_local):
        time.sleep(1)
        print(f"Seconds elapsed: {seconds_elapsed+1}")

    print("Countdown timer finished.")

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the length of countdown in seconds: "))
    except ValueError:
        print("You must enter an integer. Please try again.", file=sys.stderr)
        sys.exit(1)

    countdown_timer(seconds)
