import os
import json

# from bson.objectid import ObjectId
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

from player import Player
player = Player("bob", "location_1", "sword")


if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
@app.route("/start")
def start():
    return render_template("start.html")


@app.route("/game/<current_location>", methods=["GET", "POST"])
def game(current_location):
    if request.method == "POST":
        if request.form.get("location"):
            player.location = "location_" + request.form.get("location")
        if request.form.get("inventory"):
            player.inventory = request.form.get("inventory")

    with open("data/locations.json", "r") as r:
        data = json.load(r)
    location = data[player.location]

    return render_template("game.html", player=player, location=location)


@app.route("/victory")
def victory():
    return render_template("victory.html")


'''
@app.route("/save")
def save():
    with open("data/save_data.json", "w") as w:
        json.dumps(player)
    return redirect(url_for('game'))
'''


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
