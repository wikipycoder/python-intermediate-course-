

def greet(name): #name is a parameter here since it is passed while defining the function

    msg = f"welcome {name}"
    print(msg)


def positional_keyword(a, b, c): #positionl and keyword arguments
    print(a, b, c)


def variable_length_argument(a, b, *args, **kwargs):

    print(a)
    print(b)

    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(key, value)



def unpacking(*args):
    print(args)
    print(f"type of args {type(args)}")
    

def global_variable():
    global foo
    foo = "insert something"


def main():

    greet("John") #John is an argument here since it is being passed while calling the function
    positional_keyword(1, b=3, c=2) #Note positional arguments can not follow keyword arguments but keyword arguments can
    variable_length_argument(1, 2, 3, 4, 5, 6, seven=7, eight=8) #variable length argument and keywrod argument
    my_custom_list = {"a": 1, "b": 2, "c": 3}
    unpacking(*my_custom_list) # 

    global_variable()
    print("value of of foo", foo)




if __name__ == "__main__":
    main()