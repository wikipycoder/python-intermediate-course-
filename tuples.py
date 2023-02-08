import sys, timeit

#Typles are ordered, immutable and allow duplicate values
#Lists are tuples are very similar in nature but the only difference is that tuples can't be changed after being created.
#parenthesis are optional in tuple


def tuple_slicing():

    x = (1, 2, 3)
    y = x[1:3]
    print(x)


def tuple_vs_list_size():

    #tuples are iterables like list but they take less space in memory unlinke list
    x = 1, 2, 3
    y = [1, 2, 3]
    print("size of tuple object in memory", sys.getsizeof(x))
    print("size of list object in memory", sys.getsizeof(y))


def time_list_tuple_take():
    print(timeit.timeit(stmt="[1, 2, 3, 4]", number=1000000))
    print(timeit.timeit(stmt="1, 2, 3, 4", number=1000000))



def main():
    
    x = tuple(range(5))
    print(x)
    tuple_vs_list_size()
    time_list_tuple_take()
    # x[0] = "anyting"
    # print(x)

    # list1 = [1, 2, 3]
    # list1[0] = "something"
    # print(list1)

if __name__ == "__main__":
    main()