import todo_helper


def main():
    run=1
    todo_helper.create_table()

    while run :
        print("Press 1 :  To Add todo")
        print("Press 2 :  To Read todo")
        print("Press 3 :  To Update todo")
        print("Press 4 :  To Delete todo")
        print("Press 5 :  Exit")

        ch=input("Enter your choice: ")

        if ch == "1":
            new_todo=input("Enter your new todo: ")
            todo_helper.data_entry(new_todo)
        elif ch == "2":
            todo_helper.read_todos()
        elif ch == "3":
            id = int(input("Enter ID of todo you want to update: "))
            updated_todo=input("Enter updated todo: ")
            todo_helper.update_todo(id,updated_todo)
        
        elif ch=="4":
            id = int(input("Enter ID of todo you want to delete: "))
            todo_helper.delete_todo(id)

        elif ch=="5":
            run = 0
        else:
            print("Enter a valid option")
    todo_helper.close_connection()


if __name__ == '__main__':
    main()