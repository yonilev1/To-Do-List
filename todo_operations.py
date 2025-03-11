from enum import Enum
from datetime import *
import json
import random


class TaskStatus(Enum):
    TODO = "To Do"
    DONE = "Done"


class ToDoList:
    def __init__(self, file_name="to_do_list.json"):
        """
        Initialize the ToDoList object with a file name to store tasks.
        If the file doesn't exist, a new one will be created.

        :param file_name: The name of the file to store tasks (default is 'to_do_list.json').
        """
        self.file_name = file_name
        self.tasks = {}
        self.load_tasks()


    def load_tasks(self):
        """
        Load tasks from the file into the tasks dictionary.
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


    def get_all_tasks(self):
        """
        Return a list of all tasks in the format:
        'task_id - task_description: status'
        """
        task_list = []
        for task_id, task_info in self.tasks.items():
            task_name = task_info["task"]
            current_status = task_info["status"]
            task_list.append([task_id, task_name, current_status])
        return task_list


    def add_task(self, value, urgent):
        """
        Add a new task to the list. A unique task ID is generated, and the task is saved.

        :param value: The description of the task to be added.
        """
        task_to_add = value
        task_id = self.generate_unique_task_id()
        self.tasks[str(task_id)] = {
            "task": task_to_add,
            "status": TaskStatus.TODO.value,
            "urgency": urgent,
            "date_created": str(date.today()),
            "time_created": datetime.now().strftime("%H:%M:%S"),
            "date_done": ""
        }
        self.save_tasks()
        print(f"added task {task_to_add} successfully")


    def remove_task(self, task_num_to_remove):
        """
        Remove a task from the list by its task number.

        :param task_num_to_remove: The ID of the task to be removed.
        """
        if task_num_to_remove in self.tasks.keys():
            del self.tasks[task_num_to_remove]
            self.save_tasks()
            print(f"Task '{task_num_to_remove}' has been deleted.")
        else:
            print(f"Task '{task_num_to_remove}' was not found in the list.")


    def edit_task(self, num_task_to_edit, new_task):
        """
        Edit the description of an existing task.

        :param num_task_to_edit: The ID of the task to be edited.
        :param new_task: The new description for the task.
        """
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        if num_task_to_edit in self.tasks:
            self.tasks[num_task_to_edit]["task"] = new_task
            self.save_tasks()
            print(f"Task '{num_task_to_edit} - {new_task}' has been updated.")
        else:
            print(f"Task '{num_task_to_edit}' was not found in the list.")


    def mark_task(self, status: str, task_num_to_mark):
        """
        Mark a task as 'done' or 'todo' based on the provided status.

        :param status: The status to set for the task (either 'done' or 'todo').
        :param task_num_to_mark: The ID of the task to be marked.
        """
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        if task_num_to_mark in self.tasks:
            new_status = TaskStatus.DONE.value if status.lower() == "done" else TaskStatus.TODO.value
            self.tasks[task_num_to_mark]["status"] = new_status
            self.tasks[task_num_to_mark]["date_done"] = str(date.today()) if status.lower() == "done" else ""
            self.save_tasks()
            print(f"Task '{task_num_to_mark} - {new_status}' has been updated.")
        else:
            print(f"Task '{task_num_to_mark}' was not found.")


    def print_tasks(self, status1: str, status2=None):
        """
        Print all tasks that match the specified statuses.

        :param status1: The first status to filter tasks by.
        :param status2: An optional second status to filter tasks by.
        """
        print("in lo printing")
        table_data = []
        urgency_order = {"High": 1, "Medium": 2, "Low": 3}

        for task_number, task_info in self.tasks.items():
            task_name = task_info["task"]
            current_status = task_info["status"]
            urgency = task_info["urgency"]
            date_created = task_info["date_created"]
            date_done = task_info["date_done"] if task_info["date_done"] else "Not completed"

            if current_status.lower() == status1.lower() or (status2 and current_status.lower() == status2.lower()):
                table_data.append([task_name, current_status, urgency, date_created, date_done])

        table_data.sort(key=lambda x: (x[1] != "To Do", urgency_order.get(x[2], float('inf'))))

        return table_data


    def print_status(self, task_number):
        """
        Display the status of a specific task.

        :param task_number: The ID of the task whose status is to be checked.
        :return: The status of the task or a message if the task is not found.
        """
        #self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        try:
            if task_number in self.tasks:
                task_info = self.tasks[task_number]
                return task_info["status"]
            else:
                return "Task not found."
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
    print_done_tasks = 7
    print_tasks_to_do = 8
    print_task_status = 9
    delete_all_tasks = 10
