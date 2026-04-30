def get_todos(filepath="Todo_List.txt"):
    """Get todos from file"""
    with open(filepath, "r") as file:  # open the file and try to read to hold the existing content to append new
        todo_local = file.readlines()
    return todo_local
def write_todos(content,filePath="Todo_List.txt"):
    """Write todos to file"""
    with open(filePath, "w") as file:
        file.writelines(content)