class User:

    def __init__(self, name: str, email: str, phone: str, url: str, type: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.url = url
        self.type = type

    def getData(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "url": self.url,
            "type": self.type
        }
