# Import dummy notifs for testing
from constants import DUMMY_USER_DICT

# Factory variant creators.
from Models.ConcreteFactory import email_notif_factory, post_notif_factory, sms_notif_factory

# Custom exceptions
from Exceptions import invalid_email_req, invalid_post_req, invalid_sms_req

import unittest

from dispatcher import Dispatcher

desc = '''
    This unittest verifies instance relation.

    Since the project uses Factory design pattern for object modelling,
    it's important to make sure objects are rightly created and are instances
    of the subclass they are supposed to be of.
'''


class TestDispatcher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dummy = DUMMY_USER_DICT

    def test_email_dispatcher(self):

        # JSON with all valid attributes.
        target = TestDispatcher.dummy.get("valid_user_email")
        testIn, testOut = target.get("in").getData(), target.get("out")
        self.assertEqual(
            Dispatcher(notif_object=testIn).push_notification(),
            testOut
        )

        # JSON with only valid attributes
        target = TestDispatcher.dummy.get("none_but_essential_emailnotif")
        testIn, testOut = target.get("in").getData(), target.get("out")
        self.assertEqual(
            Dispatcher(notif_object=testIn).push_notification(),
            testOut
        )

        # JSON with missing email.
        target = TestDispatcher.dummy.get("no_email")
        testIn, testOut = target.get("in").getData(), target.get("out")
        # Since exception is handled before returning to client code,
        # using assertIsInstance() rather than assertRaises() ...
        self.assertIsInstance(
            Dispatcher(notif_object=testIn).push_notification(),
            (Exception, invalid_email_req.InvalidEmailReq)
        )

    def test_sms_dispatcher(self):
        # JSON with all valid attributes.
        target = TestDispatcher.dummy.get("valid_user_sms")
        testIn, testOut = target.get("in").getData(), target.get("out")
        self.assertEqual(
            Dispatcher(notif_object=testIn).push_notification(),
            testOut
        )

        # # JSON with only valid attributes
        # target = TestDispatcher.dummy.get("none_but_essential_emailnotif")
        # testIn, testOut = target.get("in").getData(), target.get("out")
        # self.assertEqual(
        #     Dispatcher(notif_object=testIn).push_notification(),
        #     testOut
        # )

        # # JSON with missing email.
        # target = TestDispatcher.dummy.get("no_email")
        # testIn, testOut = target.get("in").getData(), target.get("out")
        # # Since exception is handled before returning to client code,
        # # using assertIsInstance() rather than assertRaises() ...
        # self.assertIsInstance(
        #     Dispatcher(notif_object=testIn).push_notification(),
        #     (Exception, invalid_email_req.InvalidEmailReq)
        # )


if __name__ == '__main__':
    unittest.main()
