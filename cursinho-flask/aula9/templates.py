from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    x = 50
    y = 10
    query = request.args.to_dict()
    return render_template('modelo.html', x=x, z=y, query=query)#a variavel que recebe é a do jinja e a atribuida é a do python




if __name__=="__main__":
    app.run(debug=True)