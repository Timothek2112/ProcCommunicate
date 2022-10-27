from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        name = event.src_path
        name = name.split("\\")
        print(name[1])


if __name__ == "__main__":
    event_handler = EventHandler()
    observe = Observer()
    observe.schedule(event_handler, "watch", recursive=True)
    observe.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observe.stop()

    observe.join()
