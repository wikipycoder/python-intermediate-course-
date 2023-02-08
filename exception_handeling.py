

class AuthenticationError(Exception):

    def __init__(self, msg, value, *args: object) -> None:
        super().__init__(*args)
        self.msg = msg
        self.value = value


def zero_division_error(x, y):
    result = None
    try:
        result = x/y
    except ZeroDivisionError as e:
        print("0 can not be the denoominator", e)

    else: #else clause if no exception occurs
        print(result)



def index_error(*args):

    value = None
    try:
        value = args[0]
    except IndexError as e:
        print('Index error list out of range')
    

def authenticate(username="admin", password="admin"):

    try:
        raise AuthenticationError("Invalid username or password", (username, password))
    
    except AuthenticationError as e:
        print(e.msg)
        print(e.username, e.password)

    if username == "admin" and password == 'admin':
        return True

 


def assertion_error():

    is_hackable = False
    
    try:
        assert(is_hackable), "it is impossible to hack"
    except AssertionError as e:
        print(e)



def main():
    print("Exception Handeling")
    # zero_division_error(12, 0)
    # index_error()
    # authenticate("something")
    assertion_error()

if __name__ == "__main__":
    main()