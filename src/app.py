"""Main app file"""
import os

from . import create_app

app = create_app(os.getenv("CONFIG_MODE"))


@app.route("/")
def hello():
    """just testing"""
    return "Hello world!"

from .role_sessions import urls  # pylint: disable=W0611, C0413  # noqa: F401 E402,E305

if __name__ == "__main__":
    app.run()
