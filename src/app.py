"""Main app file"""
import os

from . import create_app
app = create_app(os.getenv("CONFIG_MODE"))


@app.route("/")
def hello():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
