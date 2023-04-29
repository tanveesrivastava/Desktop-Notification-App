import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Give rest to your eyes",
            message = "It's time to look away from the screen for 20 seconds so that you can blink naturally and re-moisturize your eyes.",
            app_icon = "C:\\Users\\IBMADMIN\\Documents\\Python Projects\\Desktop Notification\\eye.ico",
            timeout = 5
    )
        time.sleep(60*20)