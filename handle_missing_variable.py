data = {"a": 10, "b": 20}

key = input("Enter key: ")

try:
    print("Value:", data[key])
except KeyError:
    print("Missing variable! Key not found.")