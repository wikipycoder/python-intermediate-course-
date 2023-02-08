import copy

def compare():
    x = 10
    y = x
    y = 20
    #it wont have any impact on the values of variables since integers are immutables
    a = list()
    b = a
    a.append(1)
    #this will have impact on the values of both a and b since list is a mutable type of object in python
    print(a, b)

    list1 = [1, 2, 3]
    list2 = copy.copy(list1) #shallow copy
    list2.append(4)
    print("list1", list1)
    print("list2", list2)


    list3 = [[1, 2], [3, 4], [5, 6]]
    list4 = copy.deepcopy(list3)
    list4[0].insert(0, 0)
    print("list3", list3)
    print("list4", list4)


def main():
    print("shallow vs deep copying")
    compare()


if __name__ == "__main__":
    main()