#String: ordered, immutable, text representation


def instantiating_string():

    s1 = str()
    s2 = "just this"
    s3 = str("third way")
    print("s1", s1)
    print("s2", s2)
    print("s3", s3)


def formattin_string():
    name = "John"
    profession = "Security Analyst"
    f1 = "My name is {} and I'm a {}".format("Alex Benjimin", "Sofware Engineer")
    f2 = f"My name is {name} and I'm a {profession}"
    print(f1)
    print(f2)


def main():

    instantiating_string()
    formattin_string()


if __name__ == "__main__":
    main()