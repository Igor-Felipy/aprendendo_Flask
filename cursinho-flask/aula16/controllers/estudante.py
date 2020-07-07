from flask import Blueprint, Response, request
from ..models.estudante import db, Estudante
import json

app = Blueprint("estudantes", __name__)

@app.route('/')
def index():
    """estudantes = Estudante.query.all()
    result = [e.to_dict('id','nome','idade') for e in estudantes]"""
    rows = db.session.execute("select id, nome, idade from  estudante").fetchall()
    result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")




@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from estudante where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")



@app.route('/add', methods=["POST"])
def add():
    estudante = Estudante(str(request.form['nome']),request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return app.response_class(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")

@app.route("/edit/<int:id>", methods=["PUT","POST"])
def edite(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="applicatio/json")




@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('index'))
