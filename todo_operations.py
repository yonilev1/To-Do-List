from enum import Enum

class TaskStatus(Enum):
    TODO = "To Do"
    DONE = "Done"

class ToDoList:
    def __init__(self, file_name = "to_do_list.txt"):
        self.file_name = file_name
        self.tasks = {}
        self.load_tasks()


    def load_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    number, rest = line.strip().split(" - ", 1)
                    # task = rest.keys()[0]
                    # task, status = rest.rsplit(" : ", 1)
                    rest = rest.strip("{}").replace("'", "").replace(":", "")
                    task, status = rest.split(" ", 1)
                    self.tasks[int(number)] = {task: status}
        except FileNotFoundError:
            pass


    def save_tasks(self):
        with open(self.file_name, "w") as file:
            for number, rest in self.tasks.items():
                file.write(f"{number} - {rest}\n")


    def add_task(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            line_count = sum(1 for _ in file)
        task_to_add = input("enter a task to be added: ")
        self.tasks[line_count + 1] = {task_to_add : TaskStatus.TODO.value}
        self.save_tasks()


    def remove_task(self):
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        task_num_to_remove = int(input("Enter number of task to remove: "))
        if task_num_to_remove in self.tasks.keys():
            del self.tasks[task_num_to_remove]
            self.save_tasks()
            print(f"Task '{task_num_to_remove}' has been removed.")
        else:
            print(f"Task '{task_num_to_remove}' was not found in the list.")


    def edit_task(self):
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        task_num_to_edited = int(input("Enter the task number to edit: "))
        edited_task = input("Enter new task: ")
        if task_num_to_edited in self.tasks.keys():
            task_details = self.tasks[task_num_to_edited]
            task_status = next(iter(task_details.values()))
            self.tasks[task_num_to_edited] = {edited_task :task_status}
            print(f"Task '{task_num_to_edited} - {edited_task}' has been updated.")
        else:
            print(f"Task '{task_num_to_edited} - {edited_task}' was not found in the list.")


    def mark_task(self, status : str):
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        try:
            task_num_to_marked = int(input(f"Enter the task number to mark as {status}: "))

            if task_num_to_marked not in self.tasks:
                print(f"Task with number {task_num_to_marked} not found.")
                return
            try:
                status = status.replace(" ", "")
                new_status = TaskStatus[status.upper()].value
                item = list(self.tasks[task_num_to_marked].keys())[0]
                self.tasks[task_num_to_marked] = {item : new_status}
                print(
                    f"Task '{task_num_to_marked} - {item}' has been updated to '{new_status}'.")
                self.save_tasks()
            except ValueError:
                print(f"Invalid status '{status}'. Please choose from: {', '.join([s.value for s in TaskStatus])}")

        except ValueError:
            print("Please enter a valid task number.")


    def print_tasks(self, status1 : str, status2=None):
        for task_number, task_info in self.tasks.items():
            task_name, current_status = next(iter(task_info.items()))
            if current_status.lower() == status1.lower() or (
                    status2 is not None and current_status.lower() == status2.lower()):
                print(f"{task_number} - {task_name} : {current_status}")


    def print_status(self):
        self.print_tasks(TaskStatus.DONE.value, TaskStatus.TODO.value)
        try:
            task_number = int(input("Enter task number to check status: "))
            if task_number in self.tasks:
                task = list(self.tasks[task_number].keys())[0]
                status = list(self.tasks[task_number].values())[0]
                print(f"Task {task_number} - {task} status: {status}")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


    def delete_list(self):
        self.tasks.clear()
        open(self.file_name, "w").close()  # Empty the file
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