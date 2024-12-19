"""Main app file"""
import os

from . import create_app
from .api_bp import public_api

app = create_app(os.getenv("CONFIG_MODE"))


@app.route("/")
def hello():
    """just testing"""
    return "Hello world!"


app.register_blueprint(public_api)


if __name__ == "__main__":
    app.run()
