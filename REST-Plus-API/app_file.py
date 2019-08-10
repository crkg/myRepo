import sys
sys.path.append("/app/")
from flask import Flask
from apis import api


app = Flask(__name__)
api.init_app(app)


@api.errorhandler(Exception)
def handle_exception(error):
    return {'message': str(error)}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

