import unittest
import os
from todo_operations import ToDoList, TaskStatus

class TestToDoList(unittest.TestCase):
    def setUp(self):
        """Set up a fresh ToDoList instance before each test."""
        self.file_name = "test_to_do_list.txt"
        self.todo_list = ToDoList(self.file_name)
        self.todo_list.delete_list()  # Clean up tasks before each test

    def tearDown(self):
        """Clean up test file after tests."""
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_add_task(self):
        self.todo_list.tasks[1] = {"Test Task": TaskStatus.TO_DO.value}
        self.todo_list.save_tasks()
        self.todo_list.load_tasks()
        self.assertIn(1, self.todo_list.tasks)
        self.assertEqual(list(self.todo_list.tasks[1].keys())[0], "Test Task")

    def test_remove_task(self):
        self.todo_list.tasks[1] = {"Task to Remove": TaskStatus.TO_DO.value}
        self.todo_list.save_tasks()
        self.todo_list.remove_task()
        self.assertNotIn(1, self.todo_list.tasks)

    def test_edit_task(self):
        self.todo_list.tasks[1] = {"Old Task": TaskStatus.TO_DO.value}
        self.todo_list.save_tasks()
        self.todo_list.tasks[1] = {"New Task": TaskStatus.TO_DO.value}
        self.todo_list.save_tasks()
        self.todo_list.load_tasks()
        self.assertEqual(list(self.todo_list.tasks[1].keys())[0], "New Task")

    def test_mark_task_done(self):
        self.todo_list.tasks[1] = {"Task to Mark": TaskStatus.TO_DO.value}
        self.todo_list.save_tasks()
        self.todo_list.tasks[1] = {"Task to Mark": TaskStatus.DONE.value}
        self.todo_list.save_tasks()
        self.todo_list.load_tasks()
        self.assertEqual(list(self.todo_list.tasks[1].values())[0], TaskStatus.DONE.value)

    def test_print_tasks(self):
        self.todo_list.tasks[1] = {"Task 1": TaskStatus.TO_DO.value}
        self.todo_list.tasks[2] = {"Task 2": TaskStatus.DONE.value}
        self.todo_list.save_tasks()
        self.todo_list.load_tasks()
        self.assertEqual(len(self.todo_list.tasks), 2)

if __name__ == "__main__":
    unittest.main()
