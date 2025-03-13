# My To-Do App
A feature-rich, simple-to-use task management application built with Python, with multiple interface options.

## Overview
My To-Do App provides clean interfaces for managing your tasks. It allows you to create, edit, delete, and track the status of your tasks with customizable priorities. The application stores all tasks in a JSON file, ensuring your data persists between sessions.

## Features
- **Task Management**: Add, edit, delete, and update tasks
- **Priority Levels**: Assign Low, Medium, or High priority to tasks
- **Status Tracking**: Mark tasks as "To Do" or "Done"
- **Task Filtering**: View all tasks, only completed tasks, or only tasks that need to be done
- **Data Persistence**: All tasks are automatically saved to a file
- **Multiple Interfaces**: Choose between a GUI (using FreeSimpleGUI) or web interface (using Streamlit)
- **User-Friendly Design**: Easy-to-navigate interfaces with clear buttons and commands

## Screenshots
![GUI Interface](https://github.com/user-attachments/assets/99483c37-f5dd-4033-b498-7ba88141c149)
![GUI Interface 2](https://github.com/user-attachments/assets/6b25d5c3-2f8d-4970-9dbd-5bcfa16b4254)
![Screenshot (10)](https://github.com/user-attachments/assets/0373c234-9794-4441-bfa0-24097a14cead)
![Screenshot (9)](https://github.com/user-attachments/assets/b48c9a50-f715-48c1-b100-4727bf397288)


## Requirements
- Python 3.10 or newer (needed for match/case statements)
- FreeSimpleGUI (for GUI interface)
- Streamlit and Pandas (for web interface)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/my-todo-app.git
   cd my-todo-app
   ```
2. Install the required dependencies:
   ```bash
   # For GUI interface
   pip install FreeSimpleGUI
   
   # For web interface
   pip install streamlit pandas
   ```
3. Run the application:
   ```bash
   # For GUI interface
   python main.py
   
   # For web interface
   streamlit run app.py
   ```

## Usage

### GUI Interface
#### Adding a Task
1. Click the "Add Task" button
2. Enter the task details and select a priority level
3. Click "Save"

#### Editing a Task
1. Click the "Edit Task" button
2. Select the task you want to edit
3. Make your changes and click "Save"

#### Marking Tasks as Done/To Do
1. Click either "Mark As Done" or "Mark As To Do"
2. Select the task you want to update
3. Confirm your selection

#### Viewing Tasks
- Use "Show All Tasks" to see all tasks in the system
- Use "Show Done Tasks" to see only completed tasks
- Use "Show To Do Tasks" to see only pending tasks

#### Checking Task Status
1. Click "Show Status Task"
2. Select the task to check
3. View the status information

### Web Interface (Streamlit)
The web interface provides a modern, responsive design with all the same functionality:

1. Use the sidebar to select the operation you want to perform
2. Follow the on-screen instructions for each operation
3. Tasks are displayed in interactive tables with sorting capabilities
4. Changes are automatically saved to the same data file as the GUI interface

## Project Structure
- `main.py` - Main GUI application entry point
- `app.py` - Streamlit web interface
- `cli.py` - Command line interface operations for the to-do list
- `todo_operations.py` - Core functionality for task management
- `to_do_list.json` - Data storage file (created automatically)

## Future Enhancements
- Task due dates
- Search functionality
- Task categories and tags
- Sorting options for tasks
- Export/import functionality
- Dark mode theme
- Mobile-responsive design improvements
- Cloud synchronization

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- FreeSimpleGUI for providing an easy-to-use GUI framework
- Streamlit for enabling rapid web interface development
- All contributors who have helped improve this application
