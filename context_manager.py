


def context():

    with open("random.txt", "r") as f:
        result = f.read()
        print(result)
    
    f = open("random.txt")
    try:
        result = f.read()
        print(result)
    
    finally:
        f.close()

def main():
    print("context managers")

if __name__ == "__main__":
    main()