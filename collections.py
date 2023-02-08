from collections import Counter
from itertools import product, permutations, combinations, groupby, count, cycle, combinations_with_replacement, repeat

import time
import test

def looping():

    for i in count(1):
        print(i)
        if i == 50:
            break




def grouping_elements_on_certain_condition():

    def smaller_than_3(x):
        return x < 3



    numbers = [1, 2, 3, 4]
    result = groupby(numbers, key=smaller_than_3)

    for key, value in result:
        print(key, list(value))


def cartisian_product(a, b):

    result = product(a, b)
    return result

def counting_character_frequency():

    string = "computer architecture"
    counter = Counter(string)
    print(counter)
    print(counter.values())
    print(counter.most_common(2)) #for most common character

def main():

    # counting_character_frequency()
    # result = cartisian_product([1, 2], (3, 4))
    # print(list(result))
    # grouping_elements_on_certain_condition()
    # looping()
    print("collections.py", __name__)
    test.main()


if __name__ == "__main__":
    main()