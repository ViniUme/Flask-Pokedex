from flask import Flask, render_template
import requests
import json

class Pokemon:
    def __init__(self,id,name,type1,type2,img):
        self.id = id
        self.name = name
        self.type1 = type1

        if (type2 != None):
            self.type2 = type2
        else:
            self.type2 = ""
        self.img = img


app = Flask(__name__)

@app.route("/")
def index():
    list_pokemons = []
    id_pokemon = 1
    
    try:
        while (id_pokemon != 29):
            url = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}").text)
            name = url['forms'][0]['name']
            id = id_pokemon

            if (len(url['types']) == 2):
                type1 = url['types'][0]['type']['name']
                type2 = url['types'][1]['type']['name']
            else:
                type1 = url['types'][0]['type']['name']
                type2 = None

            img = url['sprites']['front_default']
            list_pokemons.append(Pokemon(id,name,type1,type2,img))
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