import os, json

with open("data/locations.json", "r") as r:
        data = json.load(r)

commands = ["adjacent", "door", "kill", "hello", "move"]

# Commands by name

def adjacent(target, player):
    location_data = data[player.location]
    adjacent_locations = location_data['adjacent']
    output = "You can move to the following areas: || "
    for location in adjacent_locations:
        output += " " + data[location]['name'] + " (" + location + ") |"
    output += "|"
    return output


def door(target, player):
    if target == "":
        return "I hope you're not talking to me"
    else:
        return "Killed " + target.upper() + "!"


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


def move(target, player):
    location_data = data[player.location]
    if target == "":
        return adjacent(target, player)
    elif target in data[player.location]['adjacent']:
        player.location = target
        return "You moved to " + data[player.location]['name']
    else:
        return "That is not a place you can move to."
    

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
        
    