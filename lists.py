
#Lists are ordered, mutable and allows duplicate elements

def copying_list():

    #COPYING LIST 

    list1 = [1, 2, 3] #now if we want to copy this list1 to list2 and don't want it to be updated when list2 does we must use 3 techniques
    list2 = list(list1) #one way
    list3 = list1[:] #second way
    list4 = list1.copy() #third way


def list_methods():

    #LIST OF LIST METHODS FOR DIFFERENT JOBS
    index = 3
    element = 45

    list1 = [1,2, 3] 
    list.append(4)
    list.insert(index, element)
    list.remove(3) #An exception will occur in case no element is found
    list.clear() #for clearing out the list 
    list.sort() #for sorting elements
    list.reverse()


def list_arithmetic_operation():

    list1 = list(range(1, 11))
    list2 = list1[3:4]
    list3 = list1[:]
    list4 = list1[::2] #for steping by 2
    list5 = list1[::-1]

def main():

    pass


if __name__ == "__main__":
    main()