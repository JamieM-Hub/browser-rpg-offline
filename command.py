import os, json

with open("data/locations.json", "r") as r:
        data = json.load(r)

commands = ["adjacent", "die", "door", "equip", "inventory", "kill", "hello", "load", "move", "name", "quit", "save"]

# Commands by name

def adjacent(target, player):
    location_data = data[player.location]
    adjacent_locations = location_data['adjacent']
    output = "You can move to the following areas: || "
    for location in adjacent_locations:
        output += " " + data[location]['name'] + " (" + location + ") |"
    output += "|"
    return output


def die(target, player):
    return "That's an awfully bad idea, " + player.name + ". But as they say, sometimes it's better to QUIT while you're ahead."


def door(target, player):
    if target == "":
        return "I hope you're not talking to me"
    else:
        return "Killed " + target.upper() + "!"


def equip(target, player):
    if target == "":
        output = "Your inventory: " + " ".join(player.inventory)
        # for item in player.inventory:
        #     output += [$s](item)
        return output

    elif target == player.equipped:
        return "What's in your hand?"

    elif target in player.inventory:
        player.equipItem(target)
        return "You equipped your " + target + "."

    else:
        return "One cannot equip what one does not have in one's inventory."


def hello(target, player):
    if target == "":
        return "Hello!"
    else:
        return "My name is not " + target.upper() + "."


def kill(target, player):
    if target == "":
        return "I hope you're not talking to me"
    else:
        return "Killed " + target.upper() + " at " + data[player.location]['name'] + "!"


def inventory(target, player):
    return equip("", player)


def load(target, player):
    player.loadGame()
    return "You just went back in time, " + player.name + "! Humans are crazy."


def move(target, player):
    location_data = data[player.location]
    if target == "":
        return adjacent(target, player)
    elif target in data[player.location]['adjacent']:
        print ("******************** move to " + target)
        player.changeLocation(target)
        return "You moved to " + data[player.location]['name']
    else:
        return "That is not a place you can move to."


def name(target, player):
    player.changeName(target)
    return "From now on, I shall call you " + player.name + "."


def quit(target, player):
    if target == "for-real":
        return "You wanna quit FOR-REALSIES?"
    if target == "for-realsies":
        exit()
    else:
        return "Nobody likes a quitter, " + player.name + ". That's one of the things I've learned about humans. Only the weak QUIT FOR-REAL."


def save(target, player):
    player.saveGame()
    return "I have committed your entire game to memory and can recall it for you at any time."


# Utility functions

def parse_input(input):
    input = input.split()
    try:
        return input[0], input[1]
    except:
        return input[0], ""
        

def check(input, player):
    command, target = parse_input(input)
    if command in commands:
        return eval(command + "(target, player)")
    else:
        return "unknown command or target"
        
    