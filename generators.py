

def fav_fruits(fruits=list()):

    for fruit in fruits:
        if fruit.startswith("a"):
            yield fruit
        
    yield "There is not any favourite fruit of you in the list"
        
    




def processing_time():
    pass





def main():

    data = (i for i in range(10))
    try:
        while True:
            value = next(data)
            print(value)
    except StopIteration:
        print("Stop Iteration Error")
    
    
    fruits = fav_fruits()

    print(next(fruits))




if __name__ == "__main__":
    main()