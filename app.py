import os
import json

import command
if os.path.exists("env.py"):
    import env
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from player import Player

with open("data/locations.json", "r") as r:
    data = json.load(r)

player = Player(
    "User",
    "l1",
    ["nothing"],
    "nothing",
    {
        "int_count": 0,
        "str_count": ""
    }
)


# non-Flask functions



def autosave():
    autosave = {
        "player": {
            "name": player.name,
            "location": player.location,
            "inventory": player.inventory,
            "equipped": player.equipped,
            "terminal": {
                "int_count": player.terminal['int_count'],
                "str_count": player.terminal['str_count']
            }
        }
    }
    with open("data/autosave.json", "w") as fp:
        json.dump(autosave, fp)


def clear_autosave():
    autosave = {
        # "player": {
        #     "name": player.name,
        #     "location": player.location,
        #     "inventory": player.inventory,
        #     "equipped": player.equipped,
        #     "terminal": {
        #         "int_count": player.terminal['int_count'],
        #         "str_count": player.terminal['str_count']
        #     }
        # }
    }
    with open("data/autosave.json", "w") as fp:
        json.dump(autosave, fp)


# Flask app and routes
app = Flask(__name__)


@app.route("/")
@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        player.name = request.form.get("name")
        return redirect(url_for('game'))

    return render_template("start.html")


@app.route("/load")
def load_data(player):
    with open("data/save_data.json", "r") as r:
        save_data = json.load(r)
    player.name = save_data['player']['name']
    player.location = save_data['player']['location']
    player.inventory = save_data['player']['inventory']
    player.equipped = save_data['player']['equipped']
    player.terminal['int_count'] = save_data['player']['terminal']['int_count']
    player.terminal['str_count'] = save_data['player']['terminal']['str_count']
    # print(player)
    return redirect(url_for('game'))


@app.route("/game", methods=["GET", "POST"])
def game():
    output = "..."

    if request.method == "POST":
        if request.form.get("user_input"):
            user_input = request.form.get("user_input").lower()
            output = command.processCommand(user_input, player)
            if output == None:
                output = "ERROR: output not generated"

    autosave()
    location = data[player.location]

    return render_template("game.html", player=player, location=location, output=output)


@app.route("/victory")
def victory():
    return render_template("victory.html")


@app.route("/save")
def save():
    save_data = {
        "player": {
            "name": player.name,
            "location": player.location,
            "inventory": player.inventory,
            "equipped": player.equipped,
            "terminal": {
                "int_count": player.terminal['int_count'],
                "str_count": player.terminal['str_count']
            }
        }
    }
    with open("data/save_data.json", "w") as fp:
        json.dump(save_data, fp)
    return redirect(url_for('game'))


if __name__ == "__main__":
    os.system('clear')
    print("i can has func!")
    clear_autosave()
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
