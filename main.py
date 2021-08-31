# Importing library for networking
from dispatcher import Dispatcher
import ijson

# Importing ijson for json lazy loading.
from urllib.request import urlopen
from urllib.error import URLError

# Pending notif data source URL.
PENDING_NOTIF_JSON_SOURCE = "https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json"

# Importing Notify dispatcher, which leverages the Interface for a single unified access to all Factory variants.


def main() -> None:
    try:
        pending_notif_data = ijson.items(
            urlopen(url=PENDING_NOTIF_JSON_SOURCE), 'item')
    except URLError as e:
        print(e)

    # Creating a generator for lazy retreival and avoid running out of memory.
    pending_notif_generator = (notif for notif in pending_notif_data)
    notifications_pushed = 0

    while True:
        try:
            # Fetch next value to be yielded.
            push_notif_for = next(pending_notif_generator)

            pushed_notif = Dispatcher(
                notif_object=push_notif_for).push_notification()

            print(pushed_notif)
            
            notifications_pushed += 1

        except StopIteration:
            print(
                f"JSON REDO executed sucessfully. Pushed {notifications_pushed} notifications.")
            exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("\n", "-"*30, "\nOkay, bye. <3")
