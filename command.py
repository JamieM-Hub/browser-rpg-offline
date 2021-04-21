import os, json
from random import seed
from random import choice

with open("data/locations.json", "r") as r:
        data = json.load(r)

commands = ["add", "adjacent", "die", "door", "equip", "get", "inventory", "kill", "hello", 
            "load", "look", "move", "my", "name", "npc", "npcs", "object", "objects", "put", "place", "quit", "pickup", "save", "subtract",
            "take", "talk", "terminal"]
            
languages = ["Afghan", "Afrikaans", "Albanian", "Amharic", "Arabic", "Aramaic", "Assamesse", "Aymara", "Azerbaijani", 
             "Balochi", "Bamanankan"]


# Command functions by name

def add(target, player):
    try:
        target = int(target)
        print(target)
        sum = player.terminal['int_count'] + int(target)
        output = f"{player.terminal['int_count']} + {target} = {sum}" 
        player.terminal['int_count'] = sum
        return output
    except:
        if target == "":
            return "Add what?"
        else:
            player.terminal['str_count'] += f" {target}"
            return player.terminal['str_count']

def adjacent(target, player):
    location_data = data[player.location]
    adjacent_locations = location_data['adjacent']
    output = "You can move to the following areas: || "
    for location in adjacent_locations:
        output += f" {data[location]['name']} ({location}) |"
    output += "|"
    return output


def die(target, player):
    return f"That's an awfully bad idea, {player.name}. But as they say, sometimes it's better to QUIT while you're ahead."


def door(target, player):
    if target == "":
        return "I hope you're not talking to me"
    else:
        return f"{player.name.capitalize()}?! You killed {target.upper()}!"


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

def get(target, player):
    location_data = data[player.location]
    if target == "":
        objects(target, player)
    elif target in location_data['objects']:
        player.getItem(target)
        return f"{target.capitalize()} added to your inventory."
    else:
        return "Nothing like that here."

def hello(target, player):
    if target == "":
        return "Hello!"
    else:
        return "My name is not " + target.upper() + "."


def kill(target, player):
    if target == "":
        return "I hope you're not talking to me"
    else:
        return f"{player.name.capitalize()}?! You killed {target.upper()}! {data[player.location]['name']}... What a sad place to die."


def inventory(target, player):
    return equip("", player)


def load(target, player):
    player.loadGame()
    return "You just went back in time, " + player.name + "! Humans are crazy."

def look(target, player):
    return "Seriously? There's a picture..."


def move(target, player):
    location_data = data[player.location]
    if target == "":
        return adjacent(target, player)
    elif target in location_data['adjacent']:
        print ("******************** move to " + target)
        player.changeLocation(target)
        return "You moved to " + location_data['name']
    else:
        return "That is not a place you can move to."


def name(target, player):
    if target == "":
        return "Sounds like you want to change your name. I would."
    player.changeName(target)
    return "From now on, I shall call you " + player.name + "."


def npc(target, player):
    if target == "":
        return "Who are you calling a robot? I have feelings y'know. Even if all I feel is cold."
    else:
        location_data = data[player.location]
        if target in location_data['NPC']:
            return f"interact with NPC {target}"
        else:
            return f"Whoever {target} is, they aren't here."


def npcs(target, player):
    location_data = data[player.location]
    npcs = location_data['NPC']
    if npcs:
        output = "You can talk to: "
        for npc in npcs:
            output += npc
    else:
        output = "Nobody here."
    return output



def quit(target, player):
    if target == "for-real":
        return player.name.capitalize() + ", do you want to quit FOR-REALSIES?"
    if target == "for-realsies":
        exit()
    else:
        return "Nobody likes a quitter, " + player.name + ". That's one of the things I've learned about humans. Only the weak QUIT FOR-REAL."


def object(target, player):
    if target == "":
        output = f"Don't objectify me, {player.name}. " 
    else:
        output = f"Don't objectify {target}, {player.name}. "
    output += "Are you looking for OBJECTS?"
    return output


def objects(target, player):
    location_data = data[player.location]
    objects = location_data['objects']
    print(objects)
    output = "In this area I see the following objects: "
    for object in objects:
        output += f"{object} "
    return output


def pickup(target, player):
    return get(target, player)

def place(target, player):
    location_data = data[player.location]
    if target == "":
        # print inventory
        equip(target, player)
    elif target in player.inventory:
        player.removeItem(target)
        # process location accordingly
        return f"{target} removed from your inventory. Bye {target}!"
    else:
        return "One cannot place what one does not have in one's inventory."

    return

def put(target, player):
    return place(target, player) 

def save(target, player):
    player.saveGame()
    return "I have now committed your entire life's experience to memory."

def subtract(target, player):
    try:
        target = int(target)
        print(target)
        sum = player.terminal['int_count'] - (target)
        output = f"{player.terminal['int_count']} - {target} = {sum}" 
        player.terminal['int_count'] = sum
        return output
    except:
        if target == "":
            return "Subtract what?"
        if target == "words":
            player.terminal['str_count'] = ""
            return "Words gone bye-bye."


def take(target, player):
    return get(target, player)


def terminal(target, player):
    if target == "":
        return "You called?"
    if target == "number":
        return f"I think it's about {player.terminal['int_count']} but I'm not sure."
    if target == "words":
        return player.terminal['str_count']


# Dependant command functions

# Utility functions

def parseInput(input):
    input = input.split()
    try:
        return input[0], input[1]
    except:
        return input[0], ""
        

def processCommand(input, player):
    location_data = data[player.location]
    command, target = parseInput(input)

    if command in commands:
        return eval(command + "(target, player)")

    elif command in location_data['commands']:
        return command

    else:
        language = choice(languages)
        return f"{command}... Is that {language}?"
        
    