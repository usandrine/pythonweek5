# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file and write some initial content
        with open('my_file.txt', 'w') as file:
            file.write("Hello, world!\n")
            file.write("This is a text file.\n")
            file.write("12345\n")  # Including a mix of strings and numbers
    except (PermissionError, IOError) as e:
        print(f"Error occurred while creating or writing to the file: {e}")
    finally:
        print("File creation complete.")

def read_file():
    try:
        # Read and display the contents of the file
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        print("File reading complete.")

def append_to_file():
    try:
        # Append additional lines to the file
        with open('my_file.txt', 'a') as file:
            file.write("Appending new line 1.\n")
            file.write("Appending new line 2.\n")
            file.write("Appending new line 3.\n")
    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("File appending complete.")

# Execute the functions
create_file()
read_file()
append_to_file()
read_file()  # Read again to show the appended content
