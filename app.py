import os, json, player, command

# from bson.objectid import ObjectId
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

with open("data/locations.json", "r") as r:
    data = json.load(r)

player = player.Player(
    "barry", 
    "l4", 
    "stick"
    )


if os.path.exists("env.py"):
    import env


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
        if request.form.get("location"):
            player.location = request.form.get("location")
            output = "You moved to " + data[player.location]['name'] + "."

        if request.form.get("inventory"):
            player.inventory = request.form.get("inventory")
            output = "You equipped your " + player.inventory + "."

        if request.form.get("user_input"):
            user_input = request.form.get("user_input")
            output = command.check(user_input, player)

    location_data = data[player.location]
    return render_template("game.html", player=player, location=location_data, output=output)


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
    os.system('clear')
    print("i can has func!")
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
