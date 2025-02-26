from enum import Enum
from datetime import *
import json
import random


class TaskStatus(Enum):
    TODO = "To Do"
    DONE = "Done"


class ToDoList:
    def __init__(self, file_name = "to_do_list.json"):
        """
        Initialize the ToDoList object with a file name to store tasks.
        :param file_name: Name of the file to store the tasks (default is 'to_do_list.json').
        """
        self.file_name = file_name
        self.tasks = {}
        self.load_tasks()


    def load_tasks(self):
        """
        Load the tasks from the file into the tasks dictionary.
        If the file is not found or is empty, initialize an empty task dictionary.
        """
        try:
            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = {}


    def save_tasks(self):
        """
        Save the tasks dictionary into the file as a JSON object.
        """
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)


    def generate_unique_task_id(self):
        """
        Generate a unique task ID by creating a random integer.
        :return: A unique task ID (string).
        """
        while True:
            task_id = random.randint(1000, 9999999)
            if str(task_id) not in self.tasks:
                return str(task_id)


    def add_task(self):
        """
        Prompt the user to enter a new task, assign a unique task ID,
        and add it to the tasks dictionary. Save the task list to the file.
        """
        task_to_add = input("enter a task to be added: ")
        task_id = self.generate_unique_task_id()
        self.tasks[str(task_id)] = {
            "task" : task_to_add,
            "status": TaskStatus.TODO.value,
            "date_created": str(date.today()),
            "date_done": ""
        }
        self.save_tasks()
        print(f"added task {task_to_add} successfully")


    def remove_task(self):
        """
        Display the list of tasks, prompt the user to select a task to remove,
        and delete it from the tasks dictionary. Save the updated task list to the file.
        """
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        task_num_to_remove = input("Enter number of task to remove: ")
        if task_num_to_remove in self.tasks.keys():
            del self.tasks[task_num_to_remove]
            self.save_tasks()
            print(f"Task '{task_num_to_remove}' has been removed.")
        else:
            print(f"Task '{task_num_to_remove}' was not found in the list.")


    def edit_task(self):
        """
        Display the list of tasks, prompt the user to select a task to edit,
        and update the task with a new description. Save the updated task list to the file.
        """
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        task_num_to_edit = input("Enter number of task to remove: ")
        if task_num_to_edit in self.tasks:
            new_task = input("Enter new task: ")
            self.tasks[task_num_to_edit]["task"] = new_task
            self.save_tasks()
            print(f"Task '{task_num_to_edit} - {new_task}' has been updated.")
        else:
            print(f"Task '{task_num_to_edit}' was not found in the list.")


    def mark_task(self, status : str):
        """
        Display the list of tasks, prompt the user to select a task to mark as done or not done,
        and update its status. Save the updated task list to the file.
        :param status: The status to set for the task (either 'done' or 'todo').
        """
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        task_num_to_mark = input("Enter number of task to mark: ")
        if task_num_to_mark in self.tasks:
            new_status = TaskStatus.DONE.value if status.lower() == "done" else TaskStatus.TODO.value
            self.tasks[task_num_to_mark]["status"] = new_status
            self.tasks[task_num_to_mark]["date_done"] = str(date.today()) if status.lower() == "done" else ""
            self.save_tasks()
            print(f"Task '{task_num_to_mark} - {new_status}' has been updated.")
        else:
            print(f"Task '{task_num_to_mark}' was not found.")


    def print_tasks(self, status1 : str, status2=None):
        """
        Print all tasks that match the specified status. It will display the task number,
        name, status, creation date, and completion date (if applicable).

        :param status1: The first status to filter tasks by.
        :param status2: An optional second status to filter tasks by.
        """
        for task_number, task_info in self.tasks.items():
            task_name = task_info["task"]
            current_status = task_info["status"]

            if current_status.lower() == status1.lower() or (status2 and current_status.lower() == status2.lower()):
                date_created = task_info["date_created"]
                date_done = task_info["date_done"] if "date_done" != "" else "Not completed"
                print(f"{task_number}. {task_name} | Status: {current_status} | Created: {date_created} | Completed: {date_done}")


    def print_status(self):
        """
        Display the list of tasks, prompt the user to select a task to check its status,
        and display detailed information about the task.
        """
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        try:
            task_number = input("Enter task number to check status: ").strip()

            if task_number in self.tasks:
                task_info = self.tasks[task_number]
                task_name = task_info["task"]
                current_status = task_info["status"]
                date_created = task_info["date_created"]
                date_done = task_info.get("date_done", "Not completed")

                print(f"\nTask {task_number}: {task_name}")
                print(f"Status: {current_status}")
                print(f"Created: {date_created}")
                print(f"Completed: {date_done if current_status == TaskStatus.DONE.value else 'Not completed'}")
            else:
                print("Task not found.")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")


    def delete_list(self):
        """
        Delete all tasks in the list and clear the file content.
        """
        self.tasks.clear()
        open(self.file_name, "w").close()
        print("All tasks have been deleted.")


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
    delete_all_tasks = 10