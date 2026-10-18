from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!"

@app.route("/<path:subpath>")
def page(subpath):
    if ('~' in subpath or '//' in subpath or '..' in subpath):
        return render_template("403.html"), 403
    validPath = False
    filepath = "./templates/"+subpath
    try:
        with open (filepath, 'r') as file:
            validPath = True
        file.close()
    except:
        pass
    if not validPath:
        return render_template("404.html"), 404
    else:
        return render_template(subpath)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
