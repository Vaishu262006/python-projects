# vcs.py
import os
import hashlib
import json
import shutil
import sys

REPO_DIR = ".vcs"

def init():
    if not os.path.exists(REPO_DIR):
        os.mkdir(REPO_DIR)
        os.mkdir(f"{REPO_DIR}/commits")
        with open(f"{REPO_DIR}/log.json", "w") as f:
            json.dump([], f)
        print("Repository initialized.")
    else:
        print("Repository already exists.")

def hash_file(filename):
    with open(filename, "rb") as f:
        content = f.read()
    return hashlib.sha1(content).hexdigest()

def add_and_commit(filename, message):
    if not os.path.exists(REPO_DIR):
        print("Initialize repo first: python vcs.py init")
        return
    if not os.path.exists(filename):
        print("File not found!")
        return
    file_hash = hash_file(filename)
    commit_path = f"{REPO_DIR}/commits/{file_hash}"
    shutil.copy(filename, commit_path)
    
    # update log
    with open(f"{REPO_DIR}/log.json", "r") as f:
        log = json.load(f)
    log.append({"hash": file_hash, "file": filename, "message": message})
    with open(f"{REPO_DIR}/log.json", "w") as f:
        json.dump(log, f, indent=4)
    print(f"Committed {filename} as {file_hash[:7]}")

def show_log():
    if not os.path.exists(f"{REPO_DIR}/log.json"):
        print("No commits yet.")
        return
    with open(f"{REPO_DIR}/log.json", "r") as f:
        log = json.load(f)
    for entry in reversed(log):
        print(f"{entry['hash'][:7]}: {entry['message']} ({entry['file']})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Commands: init | commit filename message | log")
        sys.exit(0)
    command = sys.argv[1]
    if command == "init":
        init()
    elif command == "commit":
        if len(sys.argv) != 4:
            print("Usage: commit filename message")
        else:
            add_and_commit(sys.argv[2], sys.argv[3])
    elif command == "log":
        show_log()