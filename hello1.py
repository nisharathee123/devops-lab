def register_patient(name, age):
    message = f"New Registration → Patient {name}, Age: {age}"
    return message


if __name__ == "__main__":
    print(register_patient("John Doe", 30))
