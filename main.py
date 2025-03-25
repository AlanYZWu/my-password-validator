import flask


# TODO: change this to your academic email
AUTHOR = "wualan@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")
    specialChars = ['!', '@', '#', '$', '%', '^', '&', '*']

    capitalCount = 0
    numCount = 0
    specialChar = False
    for char in pw:
        if char.isupper():
            capitalCount += 1
        elif char.isdigit():
            numCount += 1
        elif char in specialChars:
            specialChar = True
    
    if capitalCount < 2:
        return flask.jsonify({"valid": False, "reason": "Password must contain at least 2 capital letters"}), 400
    elif numCount < 2:
        return flask.jsonify({"valid": False, "reason": "Password must contain at least 2 digits"}), 400
    elif not specialChar:
        return flask.jsonify({"valid": False, "reason": "Password must contain at least 1 special character"}), 400
    
    return flask.jsonify({"valid": True, "reason": "Password is valid"}), 200
