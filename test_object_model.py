# Import dummy notifs for testing
from constants import DUMMY_USER_DICT

# Factory variant creators.
from Models.ConcreteFactory import email_notif_factory, post_notif_factory, sms_notif_factory

import unittest

desc = '''
    This unittest verifies instance relation.

    Since the project uses Factory design pattern for object modelling, 
    it's important to make sure objects are rightly created and are instances 
    of the subclass they are supposed to be of.
'''


class TestDispatcher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Notifier client map
        cls.NOTIFIER_CLIENTS = {
            "sms": sms_notif_factory.SmsNotifierFactory,
            "post": post_notif_factory.PostNotifierFactory,
            "email": email_notif_factory.EmailNotifierFactory,
        }

        cls.dummy = DUMMY_USER_DICT

    # Since
    def test_dispatcher_object_relation(self):
        testIn = TestDispatcher.dummy.get("valid_user").get("in")

        print("Checking dispatch for EmailNotifierFactory ...")
        self.assertIsInstance(
            TestDispatcher.NOTIFIER_CLIENTS.get("email")(testIn),
            email_notif_factory.EmailNotifierFactory,
        )

        print("Checking dispatch for SmsNotifierFactory ...")
        self.assertIsInstance(
            TestDispatcher.NOTIFIER_CLIENTS.get("sms")(testIn),
            sms_notif_factory.SmsNotifierFactory,
        )

        print("Checking dispatch for PostNotifierFactory ...")
        self.assertIsInstance(
            TestDispatcher.NOTIFIER_CLIENTS.get("post")(testIn),
            post_notif_factory.PostNotifierFactory,
        )


if __name__ == '__main__':
    print(desc)
    unittest.main()
