from todo_operations import *


my_list = ToDoList()

def get_list():
    return my_list.get_all_tasks()

def main(mission, urgency = None, value_to_add = None, number = None, edit = None):
        if mission == Options.exit.value:
            return

        if mission == Options.add_task.value:
            my_list.add_task(value_to_add, urgency)
            return

        elif mission == Options.remove_task.value:
            my_list.remove_task(number)
            return

        elif mission == Options.edit_task.value:
            my_list.edit_task(number, edit)
            return

        elif mission == Options.mark_as_done.value:
            my_list.mark_task("Done", number)
            return

        elif mission == Options.unmark_as_done.value:
            my_list.mark_task("To Do", number)
            return

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
            return

