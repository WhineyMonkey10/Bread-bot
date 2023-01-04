from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# Whenver a change in index.py is detected, restart index.py and close the old one. Also close all the nohup.out files.
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == 'index.py':
            os.system("pkill -f index.py")
            os.system("pkill -f nohup.out")
            os.system("nohup python3 index.py &")

observer = Observer()
observer.schedule(MyHandler(), path='.')
observer.start()