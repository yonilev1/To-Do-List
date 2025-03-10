import FreeSimpleGUI as sg
import cli

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
mark_done_button = sg.Button('Mark Done', size=(button_width, 1), pad=pad_value)

label_unmark = sg.Text('Enter a task to unmark: ',  size=(20, 1), pad=pad_value)
unmark_done_button = sg.Button('Unmark Done', size=(button_width, 1), pad=pad_value)

label_show_all = sg.Text('show all tasks: ',  size=(20, 1), pad=pad_value)
show_all_button = sg.Button('Show All Tasks', size=(button_width, 1), pad=pad_value)

label_print_done = sg.Text('print all Done tasks: ',  size=(20, 1), pad=pad_value)
print_done_button = sg.Button('Print Done Tasks', size=(button_width, 1), pad=pad_value)

label_print_to_do = sg.Text('print all To Do tasks: ',  size=(20, 1), pad=pad_value)
print_to_do_button = sg.Button('Print To Do Tasks', size=(button_width, 1), pad=pad_value)

label_print_status = sg.Text('Enter a task to print status: ',  size=(20, 1), pad=pad_value)
print_status_button = sg.Button('Print Status Task', size=(button_width, 1), pad=pad_value)

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

# Event loop to handle interactions
while True:
    event, values = window.read()
    print(values)  # Debug: print current values in the window
    print(event)   # Debug: print the event triggered by user interaction

    # Handle events based on button clicks
    match event:
        case 'Add Task':  # Add new task
            window_add = sg.Window("Add New Task",
                                   layout=[[sg.Text("Enter the task details:")],
                                           [sg.InputText(tooltip='Enter task name')],
                                           [sg.Button('Save'), sg.Button('Cancel')]],
                                   font=('Helvetica', 15))

            add_event, add_values = window_add.read()
            if add_event == "Save":
                cli.main(1, add_values[0])  # Call CLI to add the task

            window_add.close()

        case "Delete Task":  # Delete existing task
            tasks_list = cli.get_list()
            print(tasks_list)  # Debug: print current task list
            list_box = sg.Listbox(values=tasks_list, key='selected_task', size=(45, 10))
            window_delete = sg.Window("Delete Task",
                                      layout=[[sg.Text('Select a task to delete:'), list_box],
                                              [sg.Button('Delete Task'), sg.Button('Cancel')]],
                                      font=('helvetica', 15))

            delete_event1, delete_values1 = window_delete.read(close=True)
            print(delete_values1)  # Debug: print selected task to delete
            print(delete_event1)   # Debug: print the event triggered

            cli.main(2, "", delete_values1['selected_task'][0][0])  # Call CLI to delete the selected task

        case "Edit Task":  # Edit an existing task
            tasks_list = cli.get_list()
            print("task list: ", tasks_list)  # Debug: print task list
            list_box = sg.Listbox(values=tasks_list, key='selected_task', size=(45, 10))
            window_delete = sg.Window("Edit Task:",
                                      layout=[[sg.Text('Select a task to edit:'), list_box],
                                              [sg.Button('Edit Task'), sg.Button('Cancel')]],
                                      font=('helvetica', 15))

            edit_event1, selected_task = window_delete.read(close=True)
            print("selected tasks:", selected_task)  # Debug: print selected task for editing

            window_edit = sg.Window("Edit Task Details",
                                    layout=[[sg.Text(f"Edit the task:\n {selected_task['selected_task'][0][1]}")],
                                            [sg.InputText(tooltip='Enter a task')],
                                            [sg.Button('Save'), sg.Button('Cancel')]],
                                    font=('Helvetica', 15))

            edit_event2, edit_values2 = window_edit.read(close=True)
            print("edit_values2:", edit_values2)  # Debug: print new task details
            if edit_event2 == "Save":
                new_task = edit_values2[0]
            cli.main(3, "", selected_task['selected_task'][0][0], new_task)  # Call CLI to edit the task

        case "Mark Done":  # Mark task as done
            tasks_list = cli.get_list()
            print("task list: ", tasks_list)  # Debug: print task list
            list_box = sg.Listbox(values=tasks_list, key='selected_task', size=(45, 10))
            window_delete = sg.Window("Mark Task",
                                      layout=[[sg.Text('Select a task to mark:'), list_box],
                                              [sg.Button('Mark Task'), sg.Button('Cancel')]],
                                      font=('helvetica', 15))

            mark_event1, selected_task = window_delete.read(close=True)
            print("selected tasks:", selected_task)  # Debug: print selected task to mark
            cli.main(4, "", selected_task['selected_task'][0][0])  # Call CLI to mark the task as done

        case "Unmark Done":  # Unmark task as done
            tasks_list = cli.get_list()
            print("task list: ", tasks_list)  # Debug: print task list
            list_box = sg.Listbox(values=tasks_list, key='selected_task', size=(45, 10))
            window_delete = sg.Window("Unmark Task",
                                      layout=[[sg.Text('Select a task to Unmark:'), list_box],
                                              [sg.Button('Unmark Task'), sg.Button('Cancel')]],
                                      font=('helvetica', 15))

            unmark_event1, selected_task = window_delete.read(close=True)
            print("selected tasks:", selected_task)  # Debug: print selected task to unmark
            cli.main(5, "", selected_task['selected_task'][0][0])  # Call CLI to unmark the task

        case "Show All Tasks":  # Display all tasks
            print("in case")  # Debug: show when this case is triggered
            table_data = cli.main(6)  # Get all tasks data
            layout = [
                [sg.Text("Task List", font=("Helvetica", 16))],
                [sg.Table(values=table_data, headings=["ID", "Task", "Status", "Created Date", "Done Date"],
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

        case "Print Done Tasks":  # Display all completed tasks
            table_data = cli.main(7)  # Get done tasks data
            layout = [
                [sg.Text("Task List", font=("Helvetica", 16))],
                [sg.Table(values=table_data, headings=["ID", "Task", "Status", "Created Date", "Done Date"],
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

        case "Print To Do Tasks":  # Display all pending tasks
            table_data = cli.main(8)  # Get pending tasks data
            layout = [
                [sg.Text("Task List", font=("Helvetica", 16))],
                [sg.Table(values=table_data, headings=["ID", "Task", "Status", "Created Date", "Done Date"],
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

        case "Print Status Task":  # Print status of a specific task
            tasks_list = cli.get_list()
            print("task list: ", tasks_list)  # Debug: print task list
            list_box = sg.Listbox(values=tasks_list, key='selected_task', size=(45, 10))
            window_delete = sg.Window("Print status:",
                                      layout=[[sg.Text('Select a task to print:'), list_box],
                                              [sg.Button('Print status'), sg.Button('Cancel')]],
                                      font=('helvetica', 15))

            print_event1, selected_task = window_delete.read(close=True)
            print("selected tasks:", selected_task)  # Debug: print selected task for status

            window_edit = sg.Window("Print status Details",
                                    layout=[[sg.Text("Print status of task:")],
                                            [sg.InputText(tooltip='Enter a task')],
                                            [sg.Button('Save'), sg.Button('Cancel')]],
                                    font=('Helvetica', 15))
            number_to_print = cli.main(9, "", selected_task['selected_task'][0][0])

            layout = [
                [sg.Text("TASK STATUS", font=("Helvetica", 18, "bold"), justification='center')],
                [sg.Text(number_to_print, font=("Helvetica", 14), key="-TEXT-")],  # Display task status
                [sg.Button("Close")]
            ]

            window2 = sg.Window("Tasks", layout)

            while True:
                event, _ = window2.read()
                if event == sg.WINDOW_CLOSED or event == "Close":
                    break
            window2.close()

        case "Exit":  # Exit the application
            break

window.close()  # Close the window
