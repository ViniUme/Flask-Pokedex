from flask import Flask, render_template
import requests
import json

class Pokemon:
    def __init__(self,name,type,img):
        self.name = name
        self.type = type
        self.img = img


app = Flask(__name__)

@app.route("/")
def index():
    list_pokemons = []
    id_pokemon = 1
    
    try:
        while (id_pokemon != 500):
            url = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}").text)
            name = url['forms'][0]['name']
            type = url['types'][0]['type']['name']
            img = url['sprites']['front_default']
            list_pokemons.append(Pokemon(name, type,img))
            id_pokemon = id_pokemon + 1
    except:
        return "request erro"
    
    return render_template("index.html",
    list_pokemons = list_pokemons
    )

@app.route("/pokemon/<idPokemon>")
def pokemon(idPokemon):
    return render_template("pokemon.html", idPokemon=idPokemon)

if (__name__ == "__main__"):
    app.run(debug=True)