import FreeSimpleGUI as sg
import cli
import re

def create_main_window():
    # Define input width, button width, and padding values
    input_width = 20
    button_width = 15
    pad_value = ((10, 10), (5, 5))

    # Create labels and buttons for different actions in the to-do app
    label_add = sg.Text('Enter a task to add: ',  size=(20, 1), pad=pad_value)
    add_button = sg.Button('Add Task', size=(button_width, 1), pad=pad_value)

    label_delete = sg.Text('Enter a task to delete: ',  size=(20, 1), pad=pad_value)
    delete_button = sg.Button('Delete Task', size=(button_width, 1), pad=pad_value)

    label_edit = sg.Text('Enter a task to edit: ',  size=(20, 1), pad=pad_value)
    edit_button = sg.Button('Edit Task', size=(button_width, 1), pad=pad_value)

    label_mark = sg.Text('Enter a task to mark: ',  size=(20, 1), pad=pad_value)
    mark_done_button = sg.Button('Mark As Done', size=(button_width, 1), pad=pad_value)

    label_unmark = sg.Text('Enter a task to mark to do: ',  size=(20, 1), pad=pad_value)
    unmark_done_button = sg.Button('Mark As To Do', size=(button_width, 1), pad=pad_value)

    label_show_all = sg.Text('show all tasks: ',  size=(20, 1), pad=pad_value)
    show_all_button = sg.Button('Show All Tasks', size=(button_width, 1), pad=pad_value)

    label_print_done = sg.Text('show all Done tasks: ',  size=(20, 1), pad=pad_value)
    print_done_button = sg.Button('Show Done Tasks', size=(button_width, 1), pad=pad_value)

    label_print_to_do = sg.Text('show all To Do tasks: ',  size=(20, 1), pad=pad_value)
    print_to_do_button = sg.Button('Show To Do Tasks', size=(button_width, 1), pad=pad_value)

    label_print_status = sg.Text('Enter a task to print status: ',  size=(20, 1), pad=pad_value)
    print_status_button = sg.Button('Show Status Task', size=(button_width, 1), pad=pad_value)

    exit_button = sg.Button('Exit')

    # Listbox to display the tasks
    list_box = sg.Listbox(values=cli.get_list(), key='list of todos', enable_events=True, size=(45, 10))

    # Define the layout for the window, arranging labels and buttons
    layout = [
        [label_add, add_button],
        [label_delete, delete_button],
        [label_edit, edit_button],
        [label_mark, mark_done_button],
        [label_unmark, unmark_done_button],
        [label_show_all, show_all_button],
        [label_print_done, print_done_button],
        [label_print_to_do, print_to_do_button],
        [label_print_status, print_status_button],
        [exit_button]
    ]

    # Create the main window
    window = sg.Window("My To-Do App", layout=layout, font=('helvetica', 15))
    return window


def case_add():
    window_add = sg.Window(
        "Add New Task",
        layout=[
            [sg.Text("Enter the task details:")],
            [sg.InputText(tooltip='Enter task name', key='task_name')],
            [sg.Text("Select Priority:"), sg.Combo(["Low", "Medium", "High"], default_value="Medium", key='priority')],
            [sg.Button('Save'), sg.Button('Cancel')]
        ],
        font=('Helvetica', 15)
    )

    add_event, add_values = window_add.read()

    if add_event == "Save":
        task_name = add_values['task_name']
        priority = add_values['priority']
        cli.main(1, priority, task_name)
    window_add.close()


def case_delete():
    tasks_list = cli.get_list()
    list_box = sg.Listbox(values=tasks_list, key='selected_task', size=(45, 10))
    window_delete = sg.Window("Delete Task",
                              layout=[[sg.Text('Select a task to delete:'), list_box],
                                      [sg.Button('Delete Task'), sg.Button('Cancel')]],
                              font=('helvetica', 15))

    delete_event1, delete_values1 = window_delete.read(close=True)

    if delete_event1 == "Delete Task":
        cli.main(2, "", delete_values1['selected_task'][0][0])  # Call CLI to delete the selected task


def case_edit():
    tasks_list = cli.get_list()
    print("task list: ", tasks_list)  # Debug: print task list
    list_box = sg.Listbox(values=tasks_list, key='selected_task', size=(45, 10))
    window_delete = sg.Window("Edit Task:",
                              layout=[[sg.Text('Select a task to edit:'), list_box],
                                      [sg.Button('Edit Task'), sg.Button('Cancel')]],
                              font=('helvetica', 15))

    edit_event1, selected_task = window_delete.read(close=True)

    if edit_event1 == "Edit Task":
        window_edit = sg.Window("Edit Task Details",
                                layout=[[sg.Text(f"Edit the task:\n {selected_task['selected_task'][0][1]}")],
                                        [sg.InputText(tooltip='Enter a task')],
                                        [sg.Button('Save'), sg.Button('Cancel')]],
                                font=('Helvetica', 15))

        edit_event2, edit_values2 = window_edit.read(close=True)

        if edit_event2 == "Save":
            new_task = edit_values2[0]
            cli.main(3, "", "", selected_task['selected_task'][0][0], new_task)  # Call CLI to edit the task


def case_mark_done():
    tasks_list = cli.get_list()

    formatted_tasks = [f"{task[0]} - {task[1]} ({task[2]})" for task in tasks_list]

    list_box = sg.Listbox(values=formatted_tasks, key='selected_task', size=(45, 10))
    window_delete = sg.Window("Mark As Done",
                              layout=[[sg.Text('Select a task to mark done:'), list_box],
                                      [sg.Button('Mark Task'), sg.Button('Cancel')]],
                              font=('helvetica', 15))

    mark_event1, selected_task = window_delete.read(close=True)

    if mark_event1 == "Mark Done":
        task_number = re.search(r'\d+', selected_task['selected_task'][0]).group()
        cli.main(4, "","", task_number)  # Call CLI to mark the task as done

def case_mark_to_do():
    tasks_list = cli.get_list()

    formatted_tasks = [f"{task[0]} - {task[1]} ({task[2]})" for task in tasks_list]

    list_box = sg.Listbox(values=formatted_tasks, key='selected_task', size=(45, 10))
    window_delete = sg.Window("Mark as To Do:",
                              layout=[[sg.Text('Select a task to mark to do:'), list_box],
                                      [sg.Button('Unmark Task'), sg.Button('Cancel')]],
                              font=('helvetica', 15))

    unmark_event1, selected_task = window_delete.read(close=True)

    if unmark_event1 == "Unmark Task":
        task_number = re.search(r'\d+', selected_task['selected_task'][0]).group()
        cli.main(5, "","", task_number)  # Call CLI to unmark the task


def case_show_all():
    table_data = cli.main(6)  # Get all tasks data
    layout = [
        [sg.Text("Task List", font=("Helvetica", 16))],
        [sg.Table(values=table_data, headings=["Task", "Status", "Urgency", "Created Date", "Done Date"],
                  auto_size_columns=False, justification='left',
                  col_widths=[10, 20, 12, 12, 15], num_rows=min(10, len(table_data)),
                  key="-TABLE-")],
        [sg.Button("Close")]
    ]

    window2 = sg.Window("Tasks", layout)

    while True:
        event, _ = window2.read()
        if event == sg.WINDOW_CLOSED or event == "Close":
            break
    window2.close()


def case_show_done():
    table_data = cli.main(7)  # Get done tasks data
    layout = [
        [sg.Text("Task List", font=("Helvetica", 16))],
        [sg.Table(values=table_data, headings=["Task", "Status", "Urgency", "Created Date", "Done Date"],
                  auto_size_columns=False, justification='left',
                  col_widths=[10, 20, 12, 12, 15], num_rows=min(10, len(table_data)),
                  key="-TABLE-")],
        [sg.Button("Close")]
    ]

    window2 = sg.Window("Tasks", layout)

    while True:
        event, _ = window2.read()
        if event == sg.WINDOW_CLOSED or event == "Close":
            break
    window2.close()



def case_show_to_do():
    table_data = cli.main(8)  # Get pending tasks data
    layout = [
        [sg.Text("Task List", font=("Helvetica", 16))],
        [sg.Table(values=table_data, headings=["Task", "Status", "Urgency", "Created Date", "Done Date"],
                  auto_size_columns=False, justification='left',
                  col_widths=[10, 20, 12, 12, 15], num_rows=min(10, len(table_data)),
                  key="-TABLE-")],
        [sg.Button("Close")]
    ]

    window2 = sg.Window("Tasks", layout)

    while True:
        event, _ = window2.read()
        if event == sg.WINDOW_CLOSED or event == "Close":
            break
    window2.close()


def case_show_status():
    tasks_list = cli.get_list()
    task_list_no_id = []
    for task in tasks_list:
        task_list_no_id.append(task[1:-1])
    print("task list: ", tasks_list)  # Debug: print task list
    list_box = sg.Listbox(values=task_list_no_id, key='selected_task', size=(45, 10))
    window_print_status = sg.Window("Print status:",
                              layout=[[sg.Text('Select a task to print:'), list_box],
                                      [sg.Button('Print status'), sg.Button('Cancel')]],
                              font=('helvetica', 15))

    print_event1, selected_task = window_print_status.read(close=True)
    print("selected tasks:", selected_task)  # Debug: print selected task for status
    print(print_event1)
    if print_event1 == "Print status":

        task_number = None
        for task in tasks_list:
            print(selected_task["selected_task"][0][0], task[1])
            if selected_task["selected_task"][0][0] == task[1]:
                task_number = task[0]
                print(task_number)

        number_to_print = cli.main(9, "", "", task_number)

        layout = [
            [sg.Text("TASK STATUS", font=("Helvetica", 10, "bold"), justification='center')],
            [sg.Text(number_to_print, font=("Helvetica", 16), key="-TEXT-", justification='center')],  # Display task status
            [sg.Button("Close")]
        ]

        window2 = sg.Window("Tasks", layout)

        while True:
            event, _ = window2.read()
            if event == sg.WINDOW_CLOSED or event == "Close":
                break
        window2.close()


# Event loop to handle interactions
def main():
    window = create_main_window()
    while True:
        #window = create_main_window()
        event, values = window.read()
        print(values)  # Debug: print current values in the window
        print(event)   # Debug: print the event triggered by user interaction

        # Handle events based on button clicks
        match event:
            case 'Add Task':  # Add new task
                case_add()

            case "Delete Task":  # Delete existing task
                case_delete()

            case "Edit Task":  # Edit an existing task
               case_edit()

            case "Mark As Done":  # Mark task as done
               case_mark_done()

            case "Mark As To Do":  # Unmark task as done
                case_mark_to_do()

            case "Show All Tasks":  # Display all tasks
                case_show_all()

            case "Show Done Tasks":  # Display all completed tasks
                case_show_done()

            case "Show To Do Tasks":  # Display all pending tasks
                case_show_to_do()

            case "Show Status Task":  # Print status of a specific task
                case_show_status()

            case "Exit":  # Exit the application
                break

    window.close()  # Close the window


if __name__ == '__main__':
    main()