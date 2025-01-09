import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


host = os.environ.get("HOST", "0.0.0.0")  # Default to '0.0.0.0' if not set
port = os.environ.get("PORT", "50505")    # Default to '50505' if not set

if __name__ == '__main__':
   app.run(host=host, port=port)