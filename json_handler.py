import json


def serialization():

    global json_object

    python_dictionary = {"name": "John", "surname": "Smith", "salary": 23492374, "profession": "software engineer", "is_brilliant": True}
    json_object = json.dumps(python_dictionary)
    print("Json object", json_object)


def deserialization():

    python_dictionary = json.loads(json_object)
    print("Python object", python_dictionary)




def main():
    print("Json handler")
    serialization()
    deserialization()

if __name__ == "__main__":
    main()