import streamlit as st
import pandas as pd
from cli import operations, get_list
from todo_operations import Options

# Initialize session state
if 'refresh_state' not in st.session_state:
    st.session_state.refresh_state = False


# Define the main app
def main():
    st.title("Todo List App")

    # Sidebar for actions
    with st.sidebar:
        st.header("Actions")
        action = st.radio(
            "Choose an action:",
            [
                "View All Tasks",
                "View Tasks To Do",
                "View Completed Tasks",
                "Add New Task",
                "Edit Task",
                "Mark Task as Done",
                "Mark Task as To Do",
                "Remove Task",
                "Delete All Tasks"
            ]
        )

    # Main content area
    if action == "View All Tasks":
        view_all_tasks()
    elif action == "View Tasks To Do":
        view_todo_tasks()
    elif action == "View Completed Tasks":
        view_done_tasks()
    elif action == "Add New Task":
        add_task()
    elif action == "Edit Task":
        edit_task()
    elif action == "Mark Task as Done":
        mark_task_done()
    elif action == "Mark Task as To Do":
        mark_task_todo()
    elif action == "Remove Task":
        remove_task()
    elif action == "Delete All Tasks":
        delete_all_tasks()


def view_all_tasks():
    st.header("All Tasks")
    tasks_data = operations(Options.print_all_tasks.value)

    if tasks_data and isinstance(tasks_data, list):
        if tasks_data:
            df = pd.DataFrame(tasks_data, columns=["Task", "Status", "Urgency", "Date Created", "Date Completed"])
            st.dataframe(df)
        else:
            st.info("No tasks available.")
    else:
        st.error(f"Error retrieving tasks: {tasks_data}")


def view_todo_tasks():
    st.header("Tasks To Do")
    tasks_data = operations(Options.print_tasks_to_do.value)

    if tasks_data and isinstance(tasks_data, list):
        if tasks_data:
            df = pd.DataFrame(tasks_data, columns=["Task", "Status", "Urgency", "Date Created", "Date Completed"])
            st.dataframe(df)
        else:
            st.info("No pending tasks.")
    else:
        st.error(f"Error retrieving tasks: {tasks_data}")


def view_done_tasks():
    st.header("Completed Tasks")
    tasks_data = operations(Options.print_done_tasks.value)

    if tasks_data and isinstance(tasks_data, list):
        if tasks_data:
            df = pd.DataFrame(tasks_data, columns=["Task", "Status", "Urgency", "Date Created", "Date Completed"])
            st.dataframe(df)
        else:
            st.info("No completed tasks.")
    else:
        st.error(f"Error retrieving tasks: {tasks_data}")


def get_task_ids(status=None):
    tasks = get_list()
    if status:
        return {f"{task[0]} - {task[1]}": task[0] for task in tasks if task[2] == status}
    else:
        return {f"{task[0]} - {task[1]}": task[0] for task in tasks}

def add_task():
    st.header("Add New Task")

    task_description = st.text_input("Task Description")
    urgency = st.selectbox("Urgency", ["High", "Medium", "Low"])

    if st.button("Add Task"):
        if task_description:
            operations(Options.add_task.value, urgency=urgency, value_to_add=task_description)
            st.success(f"Task '{task_description}' added successfully!")
            st.balloons()
        else:
            st.error("Task description cannot be empty.")


def edit_task():
    st.header("Edit Task")

    task_ids = get_task_ids()

    if not task_ids:
        st.info("No tasks available to edit.")
        return

    task_selection = st.selectbox("Select a task to edit", list(task_ids.keys()))
    task_id = task_ids[task_selection]

    new_description = st.text_input("New Task Description")

    if st.button("Update Task"):
        if new_description:
            operations(Options.edit_task.value, number=task_id, edit=new_description)
            st.success(f"Task updated successfully!")
        else:
            st.error("New task description cannot be empty.")


def mark_task_done():
    st.header("Mark Task as Done")

    task_ids = get_task_ids("To Do")

    if not task_ids:
        st.info("No tasks available to mark.")
        return

    task_selection = st.selectbox("Select a task to mark as done", list(task_ids.keys()))
    task_id = task_ids[task_selection]

    if st.button("Mark as Done"):
        operations(Options.mark_as_done.value, number=task_id)
        st.success(f"Task marked as done!")


def mark_task_todo():
    st.header("Mark Task as To Do")

    task_ids = get_task_ids("Done")

    if not task_ids:
        st.info("No tasks available to mark.")
        return

    task_selection = st.selectbox("Select a task to mark as to do", list(task_ids.keys()))
    task_id = task_ids[task_selection]

    if st.button("Mark as To Do"):
        operations(Options.unmark_as_done.value, number=task_id)
        st.success(f"Task marked as to do!")


def remove_task():
    st.header("Remove Task")

    task_ids = get_task_ids()

    if not task_ids:
        st.info("No tasks available to remove.")
        return

    task_selection = st.selectbox("Select a task to remove", list(task_ids.keys()))
    task_id = task_ids[task_selection]

    if st.button("Remove Task"):
        operations(Options.remove_task.value, number=task_id)
        st.success(f"Task removed successfully!")


def delete_all_tasks():
    st.header("Delete All Tasks")

    st.warning("This action will delete all tasks permanently.")

    if st.button("Delete All Tasks", key="delete_all_button"):
        operations(Options.delete_all_tasks.value)
        st.success("All tasks have been deleted!")


if __name__ == "__main__":
    main()