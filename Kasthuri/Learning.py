from function import get_todos,write_todos


while True:
    option = input("Please type add,show,edit,complete or exit")
    option = option.lower().strip()

    if option.startswith("add"):
        todo = option[4:] +'\n'
        todo_list=get_todos()
        todo_list.append(todo)
        write_todos(todo_list)
    elif option.startswith("show"):
        todo_list = get_todos()
        for index,item in enumerate(todo_list):
            print(f"{index+1}-{item.strip()}")
    elif option.startswith("edit"):
     try:
        number = int(option[5:])
        number = number -1
        todo_list = get_todos()
        value =todo_list[number]
        prompt=f"Enter the todo to replace the {value}"
        new=input(prompt)+'\n'
        todo_list[number]=new
        print(todo_list)

        write_todos(todo_list)
     except ValueError:
        print("entered invalid value")
        continue

    elif option.startswith("complete"):
      try:
        number = int(option[9:])
        todo_list.pop(number-1)
        write_todos(todo_list)
      except ValueError:
          print("entered invalid value")
          continue

    elif option.startswith('exit'):
        print("bye!")
        break
    else :
        print("entered incorrect option")



"""
# Basic Todo list addition which will not store the data in memory
todo_list=[]

while True:
    option = input("Please type add,show,edit,complete or exit")
    option = option.lower().strip()

    match option:
        case 'add':
            todo = input("Enter todo: ")
            todo_list.append(todo)
        case 'show':
            for index,item in enumerate(todo_list):
                print(f"{index}-{item}")
        case 'edit':
            number = int(input("enter item number to update"))
            number = number -1
            value =todo_list[number]
            prompt=f"Enter the todo to replace the {value}"
            new=input(prompt)
            todo_list[number]=new
            print(todo_list)
        case 'complete':
            number = int(input("Enter item number to complete"))
            todo_list.pop(number)
            for index, item in enumerate(todo_list):
                print(f"{index+1}-{item}")
        case 'exit':
            break
        case somewhere:
            print("entered incorrect option")

"""
