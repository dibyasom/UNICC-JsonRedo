from Models.Product.email_notif import EmailNotifier
from Models.Factory.notif_factory import Creator
from Models.ConcreteFactory.sms_notif_factory import SmsNotifierFactory
from Models.ConcreteFactory.post_notif_factory import PostNotifierFactory
from Models.ConcreteFactory.email_notif_factory import EmailNotifierFactory

def client_code(creator: Creator) -> None:
    print(creator.notify_job())


def main() -> None:
    client_code(creator=SmsNotifierFactory())
    client_code(creator=PostNotifierFactory())
    client_code(creator=EmailNotifierFactory())


if __name__ == "__main__":
    main()
