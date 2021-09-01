class SomeRecoverableError(Exception):
    # Can be raised in case of any recoverable error (Not implemented yet.)
    def __init__(self, *args: object) -> None:
        super().__init__(args)