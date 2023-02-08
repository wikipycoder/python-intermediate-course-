#Dictionary: Key-Value pair, Unodered, Mutable
#Working with dictionary is cool than working with anything else

def accept_dictionary(**kwargs): #a way to accept dictionary object in a function
    print(kwargs)

def setting_different_keys():
    
    dictionary = {"name": "John Smith", ("surname", "ghostrider"): True}
    print(dictionary)


def updating_dictionary():

    developer1 = {"name": "John", "profession": "software developer"}
    developer2 = {"name": "Alex", "profession": "software developer", "company": "Google", "salary": 1000000}
    developer1.update(developer2)
    print("John", developer1)
    print("Alex", developer2)



def dictionary_instance():

    #ways to create dictionary object
    dict1 = {"name": "xyz", "security code": 23423}
    dict2 = dict(name="John", surname="Smith")
    print(dict1, "\n", dict2)

def main():
    dictionary_instance()
    accept_dictionary(name="developer1", salary=2947234972) #passing values using keyword argument
    updating_dictionary()
    setting_different_keys()



if __name__ == "__main__":
    main()