from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route("/members")
def members():
    return {"members": ["memeber 1", "member 2"]}

if __name__ == "__main__":
    app.run(debug=True)