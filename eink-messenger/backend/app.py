# Backend API entry point
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "E-Ink Messenger Backend Running"

if __name__ == "__main__":
    app.run()
