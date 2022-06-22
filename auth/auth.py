from os import getenv
from http import HTTPStatus
from flask import Flask, request, abort, make_response


app = Flask(__name__)

USERNAMES = ["one", "two", "three", "four"]


@app.route("/auth")
def auth():
    if request.args.get("name") is None or request.args.get("swfurl") is None:
        abort(HTTPStatus.BAD_REQUEST)

    username = request.args.get("name")
    idhash = request.args.get("swfurl").split("?")[-1]
    print(f"USERNAME: {username} -- IDHASH: {idhash}")

    if username in USERNAMES:
        if idhash == getenv("AUTH_STREAM_KEY"):
            return "OK", HTTPStatus.OK

    abort(HTTPStatus.UNAUTHORIZED)


if __name__ == "__main__":
    if getenv("AUTH_STREAM_KEY") is None:
        raise Exception(
            "Must set global stream key as environment variable, " +
            "AUTH_STREAM_KEY")
    app.run()
