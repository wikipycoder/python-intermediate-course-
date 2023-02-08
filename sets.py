
#set: unordered, mutable, no duplicates, not subscriptable

a = None

def instance_methods_of_set():

    global a
    a.add("abc")

    a.remove("abc") #remove an element or exepction will occur if element didn't get found otherwise
    a.discard("abc") #remove an element if it exists otherwise nothing will happen
    a.clear() #clear the set object



def updating_set():
    global a
    a.add("anonymous")
    print(a)
    # print(a[0]) #set object is not subscriptable an exception will occur in case using subscripts with a set object


def instantiating_set():
    global a
    a = {1, 2, 3, 4}
    iterable = "abc" #iterable
    b = set(iterable)
    print(a)
    print(b)


def main():

    instantiating_set()
    updating_set()


if __name__ == "__main__":
    main()