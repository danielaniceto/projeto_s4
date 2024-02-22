from src.app import app

HOST = "localhost"
PORT = 4000
DEBUG = True

if(__name__ == "__name__"):
    app.run(HOST, PORT, DEBUG)