import FreeSimpleGUI as SG
import cli
import re

def create_main_window():
    # Define input width, button width, and padding values
    button_width = 15
    pad_value = ((10, 10), (5, 5))

    # Create labels and buttons for different actions in the to-do app
    label_add = SG.Text('Enter a task to add: ', size=(20, 1), pad=pad_value)
    add_button = SG.Button('Add Task', size=(button_width, 1), pad=pad_value)

    label_delete = SG.Text('Enter a task to delete: ', size=(20, 1), pad=pad_value)
    delete_button = SG.Button('Delete Task', size=(button_width, 1), pad=pad_value)

    label_edit = SG.Text('Enter a task to edit: ', size=(20, 1), pad=pad_value)
    edit_button = SG.Button('Edit Task', size=(button_width, 1), pad=pad_value)

    label_mark = SG.Text('Enter a task to mark: ', size=(20, 1), pad=pad_value)
    mark_done_button = SG.Button('Mark As Done', size=(button_width, 1), pad=pad_value)

    label_unmark = SG.Text('Enter a task to mark to do: ', size=(20, 1), pad=pad_value)
    unmark_done_button = SG.Button('Mark As To Do', size=(button_width, 1), pad=pad_value)

    label_show_all = SG.Text('show all tasks: ', size=(20, 1), pad=pad_value)
    show_all_button = SG.Button('Show All Tasks', size=(button_width, 1), pad=pad_value)

    label_print_done = SG.Text('show all Done tasks: ', size=(20, 1), pad=pad_value)
    print_done_button = SG.Button('Show Done Tasks', size=(button_width, 1), pad=pad_value)

    label_print_to_do = SG.Text('show all To Do tasks: ', size=(20, 1), pad=pad_value)
    print_to_do_button = SG.Button('Show To Do Tasks', size=(button_width, 1), pad=pad_value)

    label_print_status = SG.Text('Enter a task to print status: ', size=(20, 1), pad=pad_value)
    print_status_button = SG.Button('Show Status Task', size=(button_width, 1), pad=pad_value)

    exit_button = SG.Button('Exit')

    # Listbox to display the tasks
    list_box = SG.Listbox(values=cli.get_list(), key='list of todos', enable_events=True, size=(45, 10))

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
    window = SG.Window("My To-Do App", layout=layout, font=('helvetica', 15))
    return window


def case_add():
    window_add = SG.Window(
        "Add New Task",
        layout=[
            [SG.Text("Enter the task details:")],
            [SG.InputText(tooltip='Enter task name', key='task_name')],
            [SG.Text("Select Priority:"), SG.Combo(["Low", "Medium", "High"], default_value="Medium", key='priority')],
            [SG.Button('Save'), SG.Button('Cancel')]
        ],
        font=('Helvetica', 15)
    )

    add_event, add_values = window_add.read()

    if add_event == "Save":
        task_name = add_values['task_name']
        priority = add_values['priority']

        if not task_name.strip():
            SG.popup_error("Task name cannot be empty!", font=('helvetica', 15))
        else:
            try:
                cli.operations(1, priority, task_name)
                SG.popup("Task added successfully!", font=('helvetica', 15))
            except Exception as e:
                SG.popup_error(f"Error adding task: {str(e)}", font=('helvetica', 15))
    window_add.close()


def case_delete():
    tasks_list = cli.get_list()
    formatted_tasks = [f"{task[0]} - {task[1]} ({task[2]})" for task in tasks_list]
    list_box = SG.Listbox(values=formatted_tasks, key='selected_task', size=(45, 10))
    window_delete = SG.Window("Delete Task",
                              layout=[[SG.Text('Select a task to delete:'), list_box],
                                      [SG.Button('Delete Task'), SG.Button('Cancel')]],
                              font=('helvetica', 15))

    delete_event1, selected_task = window_delete.read(close=True)

    if delete_event1 == "Delete Task":
        if not selected_task['selected_task']:
            SG.popup_error("No task selected! Please select a task to delete.", font=('helvetica', 15))
            return
        try:
            task_number = re.search(r'\d+', selected_task['selected_task'][0]).group()
            cli.operations(2, "", "", task_number)  # Call CLI to delete the selected task
        except (AttributeError, IndexError) as e:
            SG.popup_error(f"Error processing selection: {str(e)}", font=('helvetica', 15))


def case_edit():
    try:
        tasks_list = cli.get_list()
        if not tasks_list:
            SG.popup_error("No tasks available to edit!", font=('helvetica', 15))
            return

        formatted_tasks = [f"{task[0]} - {task[1]} ({task[2]})" for task in tasks_list]
        list_box = SG.Listbox(values=formatted_tasks, key='selected_task', size=(45, 10))
        window_delete = SG.Window("Edit Task:",
                                  layout=[[SG.Text('Select a task to edit:'), list_box],
                                          [SG.Button('Edit Task'), SG.Button('Cancel')]],
                                  font=('helvetica', 15))

        edit_event1, selected_task = window_delete.read(close=True)

        if edit_event1 == "Edit Task":
            if not selected_task['selected_task']:
                SG.popup_error("No task selected! Please select a task to edit.", font=('helvetica', 15))
                return
            try:
                task_number = re.search(r'\d+', selected_task['selected_task'][0]).group()
                task_description = ""
                for task in tasks_list:
                    if task[0] == task_number:
                        task_description = task[1]

                window_edit = SG.Window("Edit Task Details",
                                        layout=[[SG.Text(f"Edit the task:\n {task_description}")],
                                                [SG.InputText(tooltip='Enter a task')],
                                                [SG.Button('Save'), SG.Button('Cancel')]],
                                        font=('Helvetica', 15))

                edit_event2, edit_values2 = window_edit.read(close=True)

                if edit_event2 == "Save":
                    new_task = edit_values2[0]
                    if not new_task.strip():
                        SG.popup_error("Task cannot be empty!", font=('helvetica', 15))
                        return
                    cli.operations(3, "", "", task_number, new_task)
                    SG.popup("Task edited successfully!", font=('helvetica', 15))
            except (AttributeError, IndexError) as e:
                SG.popup_error(f"Error processing task edit: {str(e)}", font=('helvetica', 15))
    except Exception as e:
        SG.popup_error(f"Error in edit task window: {str(e)}", font=('helvetica', 15))

def case_mark_done():
    try:
        tasks_list = cli.get_list()
        formatted_tasks = [f"{task[0]} - {task[1]} ({task[2]})" for task in tasks_list]

        list_box = SG.Listbox(values=formatted_tasks, key='selected_task', size=(45, 10))
        window_delete = SG.Window("Mark As Done",
                                  layout=[[SG.Text('Select a task to mark done:'), list_box],
                                          [SG.Button('Mark Task'), SG.Button('Cancel')]],
                                  font=('helvetica', 15))

        mark_event1, selected_task = window_delete.read(close=True)

        if mark_event1 == "Mark Task":
            if not selected_task['selected_task']:
                SG.popup_error("No task selected! Please select a task to mark done.", font=('helvetica', 15))
                return
            try:
                task_number = re.search(r'\d+', selected_task['selected_task'][0]).group()
                cli.operations(4, "","", task_number)  # Call CLI to mark the task as done
                SG.popup("Task marked as done successfully!", font=('helvetica', 15))
            except (AttributeError, IndexError) as e:
                SG.popup_error(f"Error processing selection: {str(e)}", font=('helvetica', 15))
    except Exception as e:
        SG.popup_error(f"Error in mark task window: {str(e)}", font=('helvetica', 15))


def case_mark_to_do():
    try:
        tasks_list = cli.get_list()
        formatted_tasks = [f"{task[0]} - {task[1]} ({task[2]})" for task in tasks_list]

        list_box = SG.Listbox(values=formatted_tasks, key='selected_task', size=(45, 10))
        window_delete = SG.Window("Mark as To Do:",
                                  layout=[[SG.Text('Select a task to mark to do:'), list_box],
                                          [SG.Button('Unmark Task'), SG.Button('Cancel')]],
                                  font=('helvetica', 15))

        unmark_event1, selected_task = window_delete.read(close=True)

        if unmark_event1 == "Unmark Task":
            if not selected_task['selected_task']:
                SG.popup_error("No task selected! Please select a task to mark to do.", font=('helvetica', 15))
                return
            try:
                task_number = re.search(r'\d+', selected_task['selected_task'][0]).group()
                cli.operations(5, "","", task_number)  # Call CLI to unmark the task
                SG.popup("Task marked as to-do successfully!", font=('helvetica', 15))
            except (AttributeError, IndexError) as e:
                SG.popup_error(f"Error processing selection: {str(e)}", font=('helvetica', 15))
    except Exception as e:
        SG.popup_error(f"Error in unmark task window: {str(e)}", font=('helvetica', 15))


def case_show_all():
    try:
        table_data = cli.operations(6)  # Get all tasks data
        if not table_data:
            SG.popup_info("No tasks found!", font=('helvetica', 15))
            return

        layout = [
            [SG.Text("Task List", font=("Helvetica", 16))],
            [SG.Table(values=table_data, headings=["Task", "Status", "Urgency", "Created Date", "Done Date"],
                      auto_size_columns=False, justification='left',
                      col_widths=[10, 20, 12, 12, 15], num_rows=min(10, len(table_data)),
                      key="-TABLE-")],
            [SG.Button("Close")]
        ]

        window2 = SG.Window("Tasks", layout)

        while True:
            event, _ = window2.read()
            if event == SG.WINDOW_CLOSED or event == "Close":
                break
        window2.close()
    except Exception as e:
        SG.popup_error(f"Error showing task list: {str(e)}", font=('helvetica', 15))


def case_show_to_do_or_done(number):
    status = "Done" if number == 7 else "To Do"
    try:
        table_data = cli.operations(number)  # Get all tasks data
        if not table_data:
            SG.popup(f"No tasks {status}!", font=('helvetica', 15))
            return
        layout = [
            [SG.Text("Task List", font=("Helvetica", 16))],
            [SG.Table(values=table_data, headings=["Task", "Status", "Urgency", "Created Date", "Done Date"],
                      auto_size_columns=False, justification='left',
                      col_widths=[10, 20, 12, 12, 15], num_rows=min(10, len(table_data)),
                      key="-TABLE-")],
            [SG.Button("Close")]
        ]

        window2 = SG.Window("Tasks", layout)

        while True:
            event, _ = window2.read()
            if event == SG.WINDOW_CLOSED or event == "Close":
                break
        window2.close()
    except Exception as e:
        SG.popup_error(f"Error showing {status.lower()} tasks list: {str(e)}", font=('helvetica', 15))


def case_show_status():
    try:
        tasks_list = cli.get_list()
        if not tasks_list:
            SG.popup_error("No tasks available to show status!", font=('helvetica', 15))
            return

        task_list_no_id = []
        for task in tasks_list:
            task_list_no_id.append(task[1:-1])

        list_box = SG.Listbox(values=task_list_no_id, key='selected_task', size=(45, 10))
        window_print_status = SG.Window("Print status:",
                                        layout=[[SG.Text('Select a task to print:'), list_box],
                                                [SG.Button('Print status'), SG.Button('Cancel')]],
                                        font=('helvetica', 15))

        print_event1, selected_task = window_print_status.read(close=True)

        if print_event1 == "Print status":
            if not selected_task['selected_task']:
                SG.popup_error("No task selected! Please select a task to show status.", font=('helvetica', 15))
                return
            try:
                task_number = None
                for task in tasks_list:
                    if selected_task["selected_task"][0][0] == task[1]:
                        task_number = task[0]

                if task_number is None:
                    SG.popup_error("Could not find the selected task!", font=('helvetica', 15))
                    return

                number_to_print = cli.operations(9, "", "", task_number)

                layout = [
                    [SG.Text("TASK STATUS", font=("Helvetica", 10, "bold"), justification='center')],
                    [SG.Text(number_to_print, font=("Helvetica", 16), key="-TEXT-", justification='center')],
                    [SG.Button("Close")]
                ]

                window2 = SG.Window("Tasks", layout)

                while True:
                    event, _ = window2.read()
                    if event == SG.WINDOW_CLOSED or event == "Close":
                        break
                window2.close()
            except Exception as e:
                SG.popup_error(f"Error showing task status: {str(e)}", font=('helvetica', 15))
    except Exception as e:
        SG.popup_error(f"Error in show status window: {str(e)}", font=('helvetica', 15))


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
                case_show_to_do_or_done(7)

            case "Show To Do Tasks":  # Display all pending tasks
                case_show_to_do_or_done(8)

            case "Show Status Task":  # Print status of a specific task
                case_show_status()

            case "Exit":  # Exit the application
                break

    window.close()  # Close the window


if __name__ == '__main__':
    main()
