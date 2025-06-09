from flask import Flask
from controllers.controllers import main_blueprint

app = Flask(__name__)
app.secret_key = 'supersecreto'
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
