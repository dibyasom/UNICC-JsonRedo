'''
    Custom exception class for when data validation fails for sms.
    Will make the code robust and easier to debug.
'''

from constants import *

class InvalidEmailReq(Exception):
    def __init__(self, *args: object) -> None:
        msg : str = f"{ANSI_FAILED_NOTIF}EMAIL notifier *FAILED* [Invalid NAME or EMAIL] @ {args[0]}{ANSI_END}"
        super().__init__(msg)
