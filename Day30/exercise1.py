# Example of a try-except block

file_name = 'my_data.txt'
file = None  # Initialize to avoid NameError in finally

try:
    # FileNotFoundError exception
    # This will raise an exception the first time it runs if the file doesn't exist
    file = open(file_name, mode='r')

    # KeyError
    my_dict = {"key": "value"}
    print(my_dict["unknown_key"])

except FileNotFoundError:
    print(f"File {file_name} not found. Creating a new one...")
    with open(file_name, mode='w') as f:
        f.write("Hello World")

except KeyError as error_message:
    print(f"The key {error_message} does not exist!")

else:
    # Executed only if no exception was raised in the try block
    print("No exception raised!")
    content = file.read()
    print(content)

finally:
    # Executed always
    if file:
        print("Closing file...")
        file.close()
    else:
        print("No file to close.")