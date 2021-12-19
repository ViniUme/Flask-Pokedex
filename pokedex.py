from  flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokemon/<idPokemon>")
def pokemon(idPokemon):
    return render_template("pokemon.html", idPokemon=idPokemon)

if (__name__ == "__main__"):
    app.run(debug=True)