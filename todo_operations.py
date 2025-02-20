from enum import Enum


def add_task():
    task_to_add = input("enter a task to be added: ")
    with open("to_do_list.txt", "a") as file:
        file.write(f"{task_to_add} : To Do\n")

def remove_task():
    task_to_remove = input("Enter the task to remove: ")
    with open("to_do_list.txt", "r") as file:
        lines = file.readlines()

    lines = [line for line in lines if not line.startswith(f"{task_to_remove} :")]

    if len(lines) != len(open("to_do_list.txt", "r").readlines()):
        with open("to_do_list.txt", "w") as file:
            file.writelines(lines)
        print(f"Task '{task_to_remove}' has been removed.")
    else:
        print(f"Task '{task_to_remove}' was not found in the list.")


def edit_task():
    task_to_edited = input("Enter the task to edit: ")
    with open("to_do_list.txt", "r") as file:
        lines = file.readlines()

    task_found = False
    for i, line in enumerate(lines):
        if line.startswith(f"{task_to_edited} :"):
            task_found = True
            current_status = line.split(" : ")[1].strip()  # שמירה על הסטטוס הנוכחי
            edited_task = input("Enter the edit: ")
            lines[i] = f"{edited_task} : {current_status}\n"
            break

    if task_found:
        with open("to_do_list.txt", "w") as file:
            file.writelines(lines)
        print(f"Task '{task_to_edited}' has been updated.")
    else:
        print(f"Task '{task_to_edited}' was not found in the list.")


def mark_task(status):
    task_to_marked = input(f"Enter the task to mark as {status}: ")

    with open("to_do_list.txt", "r") as file:
        lines = file.readlines()

    task_found = False
    for i, line in enumerate(lines):
        if line.startswith(f"{task_to_marked} :"):
            task_found = True
            lines[i] = f"{task_to_marked} : {status}\n"
            break

    if task_found:
        with open("to_do_list.txt", "w") as file:
            file.writelines(lines)
        print(f"Task '{task_to_marked}' has been marked as {status}.")
    else:
        print(f"Task '{task_to_marked}' was not found in the list.")


def print_tasks(status1,status2):
    with open("to_do_list.txt", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.endswith(f"{status1}") or line.endswith(f"{status2}"):
            print(line)


def print_status():
    task = input("Enter task to be printed: ")
    task = task.strip()
    with open("to_do_list.txt", "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith(f"{task} :"):
            print(line)


def delete_list():
    with open("to_do_list.txt", "w") as file:
        file.writelines(" ")


to_do_list = {}

class Options(Enum):
    exit = 0
    add_task = 1
    remove_task = 2
    edit_task = 3
    mark_as_done = 4
    unmark_as_done = 5
    print_all_tasks = 6
    print_tasks_to_do = 7
    print_done_tasks = 8
    print_task_status = 9