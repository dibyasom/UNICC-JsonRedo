# Importing library for networking
import ijson

# Importing ijson for json lazy loading.
from urllib.request import urlopen
from urllib.error import URLError

# Importing original factory creator
from Models.Factory.notif_factory import NotifierFactory

# Factory variant creators.
from Models.ConcreteFactory.sms_notif_factory import SmsNotifierFactory
from Models.ConcreteFactory.post_notif_factory import PostNotifierFactory
from Models.ConcreteFactory.email_notif_factory import EmailNotifierFactory
from Models.User import User

# Pending notif data source URL.
PENDING_NOTIF_JSON_SOURCE = "https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json"

# Notifier client map
NOTIFIER_CLIENTS = {
    "sms": SmsNotifierFactory,
    "post": PostNotifierFactory,
    "email": EmailNotifierFactory,
}


def notifier_client(raw_data: dict) -> None:

    creator = None

    try:
        # Fetch respective function object and invoke with User arg.
        creator = NOTIFIER_CLIENTS[raw_data['type'].lower()](User(name=raw_data['name'],
                                                                  email=raw_data['email'],
                                                                  phone=raw_data['phone'],
                                                                  url=raw_data['url'],
                                                                  type=raw_data['type']))
    except KeyError as e:
        # 'type' of notifier requested by JSON object isn't supported.
        print(f"{e.args[0]} notifier service isn\'t yet supported.")

    job = creator.notify_job()


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

            notifier_client(raw_data=push_notif_for)
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
