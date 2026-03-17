Project Description
This project is a simple Git-like Version Control System built using Python.
It allows users to track changes in files, create commits, and view commit history through a command-line interface.
The main goal of this project is to understand how real version control systems such as Git work internally by implementing core functionalities from scratch using Python.
Features:
✅ Initialize a repository
✅ Track file changes
✅ Create commits with messages
✅ Store file snapshots using hashing
✅ Maintain commit history
✅ View previous commits using log command
Technologies Used:
Python
File Handling
JSON Storage
SHA-1 Hashing
Command Line Interface
How It Works:
When the repository is initialized, a hidden folder is created to store commits.
Each time a file is committed, its content is hashed and stored as a snapshot.
Commit details such as file name and message are saved in a log file.
Users can view commit history to track changes over time.
Learning Outcomes:
This project demonstrates:
Understanding of version control concepts
System design thinking
File system operations
Data structures and hashing techniques
Building real-world command-line tools
Future Improvements:
Add file restore feature
Support multiple files
Add branching functionality
Improve commit comparison
Create graphical interface
