from flask import Flask
from models.estudante import db
from controllers.estudante import app as estudante_controller

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

app.register_blueprint(estudante_controller, url_prefix="/estudante/")


if __name__=='__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)