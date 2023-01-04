# A script that automatically starts the discord bot if it goes offline
import os

# Check if the python script index.py is running
while True:
    if "python index.py" not in os.popen("ps -A").read():
        # If it is not running, start it
        os.system("python index.py")