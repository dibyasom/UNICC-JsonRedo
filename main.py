# Importing library for networking
from urllib.error import URLError
from urllib.request import urlopen

# Importing ijson for json lazy loading.
import ijson

# Importing Notify dispatcher, which leverages the Interface for a single unified access to all Factory variants.
from concurrent_dispatcher import dispatch_concurrent

# logger
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='Logs/json_redo_info.log',
                    encoding='utf-8', level=logging.DEBUG)
logging.info("Something")


# Pending notif data source URL.
PENDING_NOTIF_JSON_SOURCE = "https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json"


def openurl(url: str):
    return urlopen(url=url)


# DRIVER CODE >>>>>>>>>>
def main() -> None:
    try:
        pending_notif_data = ijson.items(
            openurl(PENDING_NOTIF_JSON_SOURCE), 'item')

    except URLError as e:
        # Network error or source is unavialable / Wrong URL.
        print('Network error or source is unavialable / Wrong URL.')
        print(e)

    # Creating a generator for lazy retreival and avoid running out of memory.
    pending_notif_generator = (notif for notif in pending_notif_data)

    while True:
        try:
            # Fetch next value to be yielded.
            push_notif_for = next(pending_notif_generator)

            # Push task to task-queue asynchronously, (returns task_id)
            pushed_notif_id = dispatch_concurrent.delay(push_notif_for)
            # Log task id.
            logging.info(
                f"Pushed {push_notif_for} | task-id: {pushed_notif_id}")

        except StopIteration:
            # JSON array parsed completely.
            print("Pushed all notifs parsed from JSON source.")
            logging.info("Pushed all notifs parsed from JSON source.")
            exit()

        finally:
            logging.shutdown()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("\n", "-"*30, "\nOkay, bye. <3")
