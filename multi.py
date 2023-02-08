from multiprocessing import Process


def greet():
    print("hey buddy")





def main():

    processes = [Process(target=greet) for i in range(10)]

    for process in processes:
        process.start()
    
    for process in processes:
        process.join()

    print("end main everything")


if __name__ == "__main__":
    main()