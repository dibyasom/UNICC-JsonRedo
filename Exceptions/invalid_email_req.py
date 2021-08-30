'''
    Custom exception class for when data validation fails for sms.
    Will make the code robust and easier to debug.
'''


class InvalidEmailReq(Exception):
    def __init__(self, *args: object) -> None:
        msg : str = f"EMAIL notifier FAILED [Invalid NAME or EMAIL] @ {args[0]}"
        super().__init__(msg)
