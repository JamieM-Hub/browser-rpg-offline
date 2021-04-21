import os
import json
import player
import command
if os.path.exists("env.py"):
    import env
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from player import Player

with open("data/locations.json", "r") as r:
    data = json.load(r)

player = Player(
    "default dave",
    "l1",
    ["", "nothing"]
)


# non-Flask functions
def load_data(player):
    with open("data/save_data.json", "r") as r:
        save_data = json.load(r)
    player.name = save_data['player']['name']
    player.location = save_data['player']['location']
    player.inventory = save_data['player']['inventory']
    player.equipped = save_data['player']['equipped']
    player.terminal['int_count'] = save_data['player']['terminal']['int_count']
    player.terminal['str_count'] = save_data['player']['terminal']['str_count']


# Flask app and routes
app = Flask(__name__)


@app.route("/")
@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        player.name = request.form.get("name")
        player.inventory = request.form.get("item")
        return redirect(url_for('game'))

    return render_template("start.html")


@app.route("/game", methods=["GET", "POST"])
def game():
    output = "..."

    if request.method == "POST":
        if request.form.get("user_input"):
            user_input = request.form.get("user_input")
            output = command.check(user_input, player)

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
    load_data(player)
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
