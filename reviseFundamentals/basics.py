def dataTypes():
    # Datatypes can be defined as the type of data that a variable can store in Python.
    # Python has the following data types built-in by default, in these categories:
    # Text Type: str
    # Numeric Types: int, float, complex
    # Sequence Types: list, tuple, range
    # Mapping Type: dict
    # Set Types: set, frozenset
    # Boolean Type: bool
    # Binary Types: bytes, bytearray, memoryview
    # You can get the data type of any object by using the type() function
    myName = "John"
    age = 36
    height = 6.1
    isMale = True
    # print(type(myName))
    # print(type(age))
    # print(type(height))
    # print(type(isMale))
    

def iterationOverData():
    myList = ["apple", "banana", "cherry"]
    myTuple = ("apple", "banana", "cherry")
    print("Iterating over List")
    for x in myList:
        print(x)
    
    print("Iterating over Tuple")
    for x in myTuple:
        print(x)
    
    # The basic difference between list and tuple is list are mutable while tuple are immutable
    # myList[0] = "orange" changes apple to orange
    # print(myList)
    # myTuple[0] = "orange" # This will throw an error
    # print(myTuple)

    # Dictionary are the datatype which store data in key value pair
    myDict = {
        "name": "John",
        "age": 36
    }
    print("Iterating over Dictionary")

    # Raises key error if key is not present
    print(myDict["age"])
    # Returns unknown if key is not present
    print(myDict.get("name","Unknown"))

def moreOperations():
    myDict = {
        "name": "John",
        "age": 36,
        "height": 6.1
        
    }


