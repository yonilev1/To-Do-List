import todo_operations
from todo_operations import *

'''def get_users_choice() -> int:
    choice = input("""
Enter 1 to add a task:
Enter 2 to remove a task:
Enter 3 to edit a task:
Enter 4 to mark a task as done:
Enter 5 to unmark a task:
Enter 6 to print all tasks:
Enter 7 to print all to do tasks:
Enter 8 to print all done tasks:
Enter 9 to print task's status:
Enter 0 to exit:\n""")

    while choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        choice = input("Invalid. Enter your choice: :")'''

    #return int(choice)

my_list = todo_operations.ToDoList()

def get_list():
    return my_list.get_all_tasks()

def main(mission, value_to_add = None, number = None, edit = None):
    #my_list = todo_operations.ToDoList()
    while True:
        #mission = get_users_choice()
        if mission == Options.exit.value:
            break

        if mission == Options.add_task.value:
            my_list.add_task(value_to_add)
            break

        elif mission == Options.remove_task.value:
            my_list.remove_task(number)
            break

        elif mission == Options.edit_task.value:
            my_list.edit_task(number, edit)
            break

        elif mission == Options.mark_as_done.value:
            my_list.mark_task("Done", number)
            break

        elif mission == Options.unmark_as_done.value:
            my_list.mark_task("To Do", number)
            break

        elif mission == Options.print_all_tasks.value:
            print("in cli printing all")
            return my_list.print_tasks("To Do", "Done")

        elif mission == Options.print_tasks_to_do.value:
            return my_list.print_tasks("To Do", "H")

        elif mission == Options.print_done_tasks.value:
            return my_list.print_tasks("Done", "H")

        elif mission == Options.print_task_status.value:
            return my_list.print_status(number)


        elif mission == Options.delete_all_tasks.value:
            my_list.delete_list()
            break

    print("Exit program.")

if __name__ == '__main__':
    main()

