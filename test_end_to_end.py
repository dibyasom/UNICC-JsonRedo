'''
    Main code depends on fetching JSON array from provided URL, sometimes external factors (Network, server down, etc)
    may fail the test cases, hence this end-to-end test uses mocking.
'''

import unittest
from unittest.mock import patch

import main

# Data for mocking
from constants import DUMMY_USER_JSON_ARRAY


class Mock():
    def __init__(self, request, context):
        return None

    def read(self):
        return self

    def decode(self, arg):
        return ''

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration


class TestEndToEnd(unittest.TestCase):

    def test_end_to_end(self):
        with patch('urllib.request.urlopen', Mock) as mocked_get:
            mocked_get.return_value = DUMMY_USER_JSON_ARRAY

            # Implementing test here.
