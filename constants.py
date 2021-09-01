# Delay simulated by mock functions.
from Models.User import User
SIMULATED_NETWORK_DELAY: float = 0.5

#  ANSI escape codes.
# **************************

# Failed to push notif.
# 0-Simple text-styling, 37-white color, 41m-red bg.
ANSI_FAILED_NOTIF = '\033[0;37;41m'
ANSI_FAILED_NOTIF = ''

# Notif pushed successfully.
# Simple text-style, black color, green-bg.
ANSI_SUCCESS_NOTIF = '\033[0;30;42m'
ANSI_SUCCESS_NOTIF = ''

# End ANSI leak (Transparent bg)
ANSI_END = '\033[0;30;49m'
ANSI_END = ''

# **************************


# Dummy user dict for testing including edge cases.
DUMMY_USER_DICT = {
    "valid_user_email": {
        'in': User(
            name='Dibyasom Puhan',
            email='dibyasom@calcul.ai',
            phone='+919668766409',
            url="https://www.toptiersecurity.com",
            type='email'
        ),
        'out': "EMAIL sent to dibyasom@calcul.ai. Data: {'name': 'Dibyasom Puhan', 'email': 'dibyasom@calcul.ai', 'phone': '+919668766409', 'url': 'https://www.toptiersecurity.com', 'type': 'email'}"
    },
     "valid_user_sms": {
        'in': User(
            name='Dibyasom Puhan',
            email='dibyasom@calcul.ai',
            phone='+919668766409',
            url="https://www.toptiersecurity.com",
            type='sms'
        ),
        'out': "SMS sent to +919668766409. Data: {'name': 'Dibyasom Puhan', 'email': 'dibyasom@calcul.ai', 'phone': '+919668766409', 'url': 'https://www.toptiersecurity.com', 'type': 'sms'}"
    },
    "no_email": {
        'in': User(
            name='Dibyasom Puhan',
            email=None,
            phone='+919668766409',
            url="https://www.toptiersecurity.com",
            type='email'
        ),
        'out': "EMAIL notifier *FAILED* [Invalid NAME or EMAIL] @ {'name': 'Dibyasom Puhan', 'email': None, 'phone': '+919668766409', 'url': None, 'type': 'email'}",
    },
    "no_name": User(
        name=None,
        email='dibyasom@calcul.ai',
        phone='+919668766409',
        url=None,
        type='email'
    ),
    "no_type": User(
        name='Dibyasom Puhan',
        email='dibyasom@calcul.ai',
        phone='+919668766409',
        url=None,
        type=None
    ),
    "none_but_essential_emailnotif": {
        'in': User(
            name='Dibyasom Puhan',
            email='dibyasom@calcul.ai',
            phone=None,
            url=None,
            type='email'
        ),
        'out': "EMAIL sent to dibyasom@calcul.ai. Data: {'name': 'Dibyasom Puhan', 'email': 'dibyasom@calcul.ai', 'phone': None, 'url': None, 'type': 'email'}"
    },
}

# ****************************************

DUMMY_USER_JSON_ARRAY = [
    {
        "name": "Brent Valdez",
        "email": "annagregory@example.org",
        "phone": "139.386.6589",
        "url": "https://ayers-perry.com/",
        "type": "email"
    },
    {
        "name": "Jonathan Green",
        "email": None,
        "phone": "(245)765-5361x8165",
        "url": None,
        "type": "email"
    },
    {
        "name": "Barbara Donovan",
        "email": "richardhoffman@example.com",
        "phone": "347-725-8534",
        "url": None,
        "type": "post"
    },
    {
        "name": "Barbara Donovan",
        "email": "richardhoffman@example.com",
        "phone": "347-725-8534",
        "url":  "https://www.url.com",
        "type": "post"
    },
    {
        "name": "Stephanie Martin",
        "email": "rodriguezstephanie@example.org",
        "phone": "001-621-651-0995x703",
        "url": "https://www.nunez.com/",
        "type": "sms"
    },
]