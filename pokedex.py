from nturl2path import url2pathname
from webbrowser import get
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
@app.route("/home")
def home():
    
    list_pokemons = []
    const_id = 26
    id_pokemon = 1
    
    while (id_pokemon != const_id):
        try:
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
    
    return render_template("home-pokepage.html",
    list_pokemons = list_pokemons
    )

@app.route("/home/pokepage<id_page>")
def pokepage(id_page):
    
    list_pokemons = []
    
    if (int(id_page) == 36):
        
        const_id = 899
        id_pokemon = 876
        
        while (id_pokemon != const_id):
            try:
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
        
        return render_template("home-pokepage.html",
        list_pokemons = list_pokemons
        )
        
    else:
        
        const_id = int(id_page) * 25 + 1
        id_pokemon = const_id - 25
        
        while (id_pokemon != const_id):
            try:
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
        
        return render_template("home-pokepage.html",
        list_pokemons = list_pokemons
        )

@app.route("/pokemon/<id_pokemon>")
def PokemonStatus(id_pokemon):
    url = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}").text)

    return render_template("pokemon-status.html", url = url)


if (__name__ == "__main__"):
    app.run(debug=True)