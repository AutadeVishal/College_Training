import re

class InvalidEmailError(Exception):
    def __init__(self, email):
        super().__init__(f"Invalid email format: '{email}'")

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailError(email)
    return True

try:

    check_email("student@dfsa.edu")
    print("Email is valid.")
    check_email("not-an-@email.asd")
except InvalidEmailError as e:
    print(e)

