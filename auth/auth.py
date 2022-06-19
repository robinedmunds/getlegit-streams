from os import getenv
from http import HTTPStatus
from flask import Flask, request, abort, make_response


app = Flask(__name__)
credentials = {
    "users": getenv("CREDENTIALS_USERS"),
    "key": getenv("CREDENTIALS_KEY")
}


@app.route("/auth")
def auth():
    if request.args.get("name") is None or request.args.get("swfurl") is None:
        abort(HTTPStatus.BAD_REQUEST)

    username = request.args.get("name")
    idhash = request.args.get("swfurl").split("?")[-1]
    print(f"USERNAME: {username} -- IDHASH: {idhash}")

    # TODO: store usernames and key in env vars
    if username in ["one", "two", "three", "four"]:
        if idhash == "biglongpassword":
            return "OK", HTTPStatus.OK

    abort(HTTPStatus.UNAUTHORIZED)


if __name__ == "__main__":
    app.run()
