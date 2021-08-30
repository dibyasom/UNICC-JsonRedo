from Models.Product.email_notif import EmailNotifier
from Models.Factory.notif_factory import Creator
from Models.ConcreteFactory.sms_notif_factory import SmsNotifierFactory
from Models.ConcreteFactory.post_notif_factory import PostNotifierFactory
from Models.ConcreteFactory.email_notif_factory import EmailNotifierFactory
from Models.User import User


def client_code(creator: Creator) -> None:
    job = creator.notify_job()
    if job:
        print(job)


def main() -> None:

    client_code(creator=SmsNotifierFactory(User(name="Dibyasom Puhan",
                email="dibya.secret@gmail.com", phone='9668766409', url="www.google.com", type="sms")))
    client_code(creator=PostNotifierFactory(User(name="Dibyasom Puhan",
                email="dibya.secret@gmail.com", phone='9668766409', url="www.google.com", type="url")))
    client_code(creator=EmailNotifierFactory(User(name="Dibyasom",
                email=None, phone='9668766409', url="www.google.com", type="mail")))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("\n", "-"*30, "\nOkay, bye. <3")
