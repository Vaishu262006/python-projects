# ai_assistant.py
import json
import os
import math

TASKS_FILE = "tasks.json"

# Load tasks
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks.append(task)
    save_tasks()
    print(f"Task added: {task}")

def list_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")

def solve_math(expr):
    try:
        result = eval(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        cmd = input("> ").strip()
        if cmd.startswith("add_task"):
            add_task(cmd[9:].strip())
        elif cmd=="list_tasks":
            list_tasks()
        elif cmd.startswith("solve_math"):
            solve_math(cmd[11:].strip())
        elif cmd=="exit":
            break
        else:
            print("Commands: add_task, list_tasks, solve_math, exit")

if __name__ == "__main__":
    main()