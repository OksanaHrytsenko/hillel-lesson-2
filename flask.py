from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    response = make_response(jsonify(request.args))
    for k, v in request.args.items():
        response.set_cookie(k, v)
    return response


if __name__ == "__main__":
    app.run()
