from todo_operations import *

def main():
    mission = int(input("""
Enter 1 to add a task:
Enter 2 to remove a task:
Enter 3 to edit a task:
Enter 4 to mark a task as done:
Enter 5 to unmark a task:
Enter 6 to print all tasks:
Enter 7 to print all to do tasks:
Enter 8 to print all done tasks:
Enter 9 to print task's status:
Enter 0 to exit:\n"""))

    while mission != Options.exit:

        if mission == Options.add_task.value:
            add_task()

        elif mission == Options.remove_task.value:
            remove_task()

        elif mission == Options.edit_task.value:
            edit_task()

        elif mission == Options.mark_as_done.value:
            mark_task("Done")

        elif mission == Options.unmark_as_done.value:
            mark_task("To Do")

        elif mission == Options.print_all_tasks.value:
            print_tasks("To Do\n", "Do\n")

        elif mission == Options.print_tasks_to_do.value:
            print_tasks("To Do\n", "A")

        elif mission == Options.print_done_tasks.value:
            print_tasks("Done\n", "A")

        elif mission == Options.print_task_status.value:
            print_status()

        mission = int(input("Enter Your choice: "))
        if mission not in range(0, 10):
            mission = int(input("Not valid choice, Enter another choice: "))
    delete_list()

if __name__ == '__main__':
    main()