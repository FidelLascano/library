import flask
from controller import book_controller
if __name__ == '__main__':
    app = flask.Flask(__name__)
    app.register_blueprint(book_controller.book)

    app.run(debug=True, port=8899)