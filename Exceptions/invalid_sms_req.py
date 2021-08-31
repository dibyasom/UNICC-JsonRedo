'''
    Custom exception class for when data validation fails for sms.
    Will make the code robust and easier to debug.
'''

from constants import *

class InvalidSmsReq(Exception):
    def __init__(self, *args: object) -> None:
        msg: str = f"{ANSI_FAILED_NOTIF}SMS notifier *FAILED*  [Invalid NAME or PHONE] @ {args[0]}{ANSI_END}"
        super().__init__(msg)
