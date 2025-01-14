import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

print("starting the app")

def print_directory_tree(path="/", indent=""):
    # List all files and directories in the current path
    with os.scandir(path) as entries:
        for entry in entries:
            # Check if entry is a directory
            if entry.is_dir():
                print(indent + f"[DIR] {entry.name}")
                # Recursively print the tree for subdirectories
                print_directory_tree(entry.path, indent + "  ")


@app.route('/')
def index():
   print('Request for index page received')
   print_directory_tree()
   return render_template('index.html')


host = os.environ.get("HOST", "0.0.0.0")  # Default to '0.0.0.0' if not set
port = os.environ.get("PORT", "50505")    # Default to '50505' if not set

if __name__ == '__main__':
   print("run app...")
   app.run(host=host, port=port)
