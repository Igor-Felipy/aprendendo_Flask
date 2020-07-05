from flask import Flask, render_template, request, url_for, redirect,Response
from modules import db, Estudante
import json

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'


@app.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/add', methods=["POST"])
def add():
    estudante = Estudante(str(request.form['nome']),request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return app.response_class(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edite(id):
    estudante = Estudante.query.get(id)
    if request.method == "POST":
        estudante.nome = request.form['nome']
        estudante.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', estudante=estudante)



@app.route('/delete/<int:id>')
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('index'))

if __name__=='__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)