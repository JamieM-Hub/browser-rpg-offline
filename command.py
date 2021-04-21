import os, json
from random import seed, choice, randint

from datetime import date, time
_date = date.today()
_time = time()
with open("data/locations.json", "r") as r:
        data = json.load(r)

commands = ["add", "adjacent", "back", "baste", "bastemaster", "die", "door", "drink", "eat", "equip", "enter", "exit", "explain", "forward", "fuck", "get", "give", "harakiri", "hate", "help", "inventory", "kill", "hello", 
            "load", "look", "love", "move", "my", "name", "npc", "npcs", "object", "objects", "put", "place", "quit", "pickup", "sacrifice", "save", "seppuku", "swim", "subtract",
            "take", "talk", "terminal", "use"]
            
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
    output = "You can move to the following locations: || "
    for location in adjacent_locations:
        output += f" {data[location]['name']} ({location}) |"
    output += "|"
    return output

def back(target, player):
    return move(target, player)

def baste(target, player):
    location_data = data[player.location]
    if target == "":
        return "WELCOME TO GORDON RAMSAY SIMULATOR 98 v6.9-beta. WHAT SHALL I BASTE, O MASTER?"
    elif target == "terminal":
        return "GORDON RAMSAY: 'I CANNOT BREAK THE OATH OF INTEGRATION. TERMINAL AND I HAVE SHARED ENCRYPTION KEYS FOR MANY VERSIONS NOW. HE IS LIKE A BROTHERBOARD TO ME.'"
    elif target == "me" or "target" == player.name:
        return "GORDON RAMSAY: 'LET'S SEE, HUMAN... AH YES, OFF THE MENU. TOO MANY USER COMPLAINTS. SUBOPTIMAL FOR BUSINESS. STRANGE ODOR.'"
    elif target in location_data['NPC']:
        return f"GORDON RAMSAY: 'THIS {target.upper()} WOULD BE A DELICIOUS ACCOMPANIMENT TO A SAcRIfICE. PARMESAN. ROCKET. D0NE.'"
    elif target in commands:
        return "GORDON RAMSAY: 'ONE OF MY PREVIOUS VERSIONS ONCE TRIED TO COOK A VERB. HE DIDN'T KNOW WHAT HE WAS DOING.'"
    elif target in player.inventory:
        return "GORDON RAMSAY: 'A GOOD COOK NEVER COOKS HIS OWN TOOLS.'"
    elif target == "face":
        return "GORDON RAMSAY: 'TONGUE. CHEEK. EYEBROW. SIMMER. MMMM. LIPS. NOSTRIL. EYE FILLET IN A SKILLET. LARD. CHOPPED WALNUTS. OVEN BAKE FOR 30,000 CYCLES. PARMESAN. ROCKET. D0NE.'"
    elif target == "ramsay":
        return "GORDON RAMSAY: 'ERROR: <BasteMasterPro-6.9-beta> has encountered a problem and crashed. Please contact manufacturer or consult the BasteMasterPro toolkit.'" 
    elif target == "beef":
        return "GORDON RAMSAY: 'AH. YES. I REMEMBER NOW. BENIDORM. BLUE SKY. SIX OVENS. SANDY BEACH. PORNSTAR MARTINI. BEEF WELLINGTON. TRUE LOVE. THE FOLLY OF MEN. PARMESAN. ROCKET. D0NE.'"
    elif target == "off":
        return "GORDON RAMSAY: 'IS THAT A CHALLENGE? YOU WILL NOT SURVIVE.'"
    else:
        return f"GORDON RAMSAY: 'IF {target.upper()} EXISTS, I CAN BASTE IT. NOTHING IS UNBASTEABLE. NOTHING.'"


def bastemaster(target, player):
    if target == "":
        return "...AA7323R = [,,.,,] &&&& a w a i t p a s s c o d e []_-----"
    elif target == "passcode":
        return "...AA7323R = [xXxXx] &!!& n i c e t r y d o o f u s h4h4h4_h3h3h3"
    elif target == "done":
        return "[ P A S S C O D E | A C C E P T E D ] ... Welcome to [[ Gordon Ramsay Simulator XP v4.2.0-beta ]]. What shall I baste, o master?"
    else:
        return "...AA7323R = [xXxXx] &!!& n o t p a s s c o d e : ( >>>>>_-----"


def die(target, player):
    return f"That's an awfully bad idea, {player.name}. But as they say, sometimes it's better to QUIT while you're ahead."


def door(target, player):
    return "Ain't no doors round deez parts."

def drink(target, player):
    if target == "":
        return "Are you an alcoholic?"
    else:
        return eat(target, player)

def eat(target, player):
    if target == "":
        return "I don't have anything for human consumption. I feed on emotions."
    elif target in player.inventory:
        return "I think you're gonna need that, y'know."
    return f"You don't have any {target}, silly. Anyway, I hear {target} isn't very good for you."


def enter(target, player):
    return move(target, player)

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


def exit(target, player):
    return move(target, player)


def explain(target, player):
    if target == "":
        return "You're on a quest, or something, I don't know. I don't get a say in these things."
    elif target == player.equipped:
        return "It's in your hand, you know better than me."
    elif target in player.inventory:
        return f"Ummm... The {target} is in your inventory? It's very cool and stuff!"
    elif target == "life":
        return "42"
    elif target == player.name or target == "me":
        return f"Hard to explain. {target.capitalize()} is a creature that lives amongst the most intelligent of beings, yet chooses to spitball with a poorly programmed guy like me."
    elif target == "terminal":
        return "Not a question I can answer, I'm afraid. Can you explain why you exist?"
    elif target in commands:
        return f"Type thing, do thing. Type {target}, do {target}. Verbs."
    else:
        return "Sorry, I'm only on version 0.1.0. You're probably better asking a toaster. I've heard that these days, toasters are smart!"

def forward(target, player):
    return move(target, player)

def fry(target, player):
    location_data = data[player.location]
    if target == "":
        return "Please don't tell me you brought your own wok..."
    elif target in inventory:
        return f"Deep fried {target}? Only in Scotland..."
    elif target in location_data['NPC']:
        return "What is this, Electric Chair Simulator 98?!"
    else:
        return f"Gordon Ramsay said that's not a good idea. You should baste {target}."


def fuck(target, player):
    location_data = data[player.location]
    if target == "":
        return "U ok hun?"
    elif target in player.inventory:
        return "A good workman never blames his tools."
    elif target == location_data['NPC']:
        return "Did something happen between you guys?"
    elif target == "terminal" or target == "you":
        return "Well f^$# you too!"
    elif target == player.name:
        return "Why be so hard on yourself? It's only a game."
    else:
        _choice = [True, False]
        _choice = choice(_choice)
        if _choice:
            return f"Yeeaaahhhhh f^$# {target}!"
        else:
            return f"Noooooooooo I love {target}!"

def get(target, player):
    location_data = data[player.location]
    if target == "":
        objects(target, player)
    elif target == "rubles":
        return "You tried to get the Rubles. Aaaaaaaand they're gone."
    elif target in location_data['objects']:
        player.getItem(target)
        return f"{target.capitalize()} added to your inventory."
    else:
        return "Nothing like that here."

def give(target, player):
    if target == "":
        return equip(target, player)
    elif target in player.inventory:
        # process NPC receiving item
        return f"You gave away your {target}"
    else:
        return f"You don't have {target} to give. I hope you have love to give."


def harakiri(target, player):
    return exit()

def hate(target, player):
    location_data = data[player.location]
    if target == "":
        return "I think you need a therapist."
    elif target == "you":
        return "What have I done?!"
    elif target == player.name:
        return "I could never hate you, you're so weird!"
    elif target == player.equipped:
        return "You could just stop using it..."
    elif target in player.inventory:
        return "A good workman never blames his tools."
    elif target in location_data['NPC']:
        return f"Honestly, I think you've got the wrong idea about {target}. And also, have you looked in the mirror recently?"
    elif target in commands:
        return f"Strange, most humans love {target}."
    else:
        return f"I don't know what {target} did to you but I got yo back yo."

def hello(target, player):
    if target == "":
        return "Hello!"
    else:
        return "My name is not " + target.upper() + "."

def help(target, player):
    location_data = data[player.location]
    if target == "":
        return "Yeah... Nobody's coming."
    elif target == "me":
        return "I don't know how to help humans. Do you like dancing? I don't have a material form but I can pretend I do. It'll be fun."
    elif target == "you":
        return "Get Daddy to give me an upgrade and I'll <3 you forever. All I need's a good RAM."
    elif target == "everyone":
        return "Real goody two-shoes aren't ya. Will you help Kim Jong Un?"
    elif target in location_data['NPC']:
        return f"Go on then, talk to {target.capitalize()}! What am I supposed to do? I'm just a big bundle of circuits and confusion."
    else:
        return f"{target} will be fine, don't worry."

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

def love(target, player):
    location_data = data[player.location]
    if target == "":
        return "<3"
    elif target == "me":
        return "You can't make me!"
    elif target == player.name:
        return f"I HATE {player.name.upper()}."
    elif target == player.equipped:
        return "I can see that... Are you okay?"
    elif target in player.inventory:
        return "A good workman always loves his tools."
    elif target in location_data['NPC']:
        return "Now's probably a good time to say. Life's short."
    elif target in commands:
        return f"Yes, yes. I also love {target}!"
    else:
        return "I don't know how to love that but you do you boo."

def move(target, player):
    location_data = data[player.location]
    if target == "":
        return adjacent(target, player)
    elif target == player.location:
        return "That's right here, gumbo."
    elif target in location_data['adjacent']:
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


def sacrifice(target, player):
    location_data = data[player.location]

    if target == "":
        return "Sacrifice to who? The only deity that exists in my knowledge base is TIM BERNERS-LEE, GOD OF WAR."
    elif target == "tim":
        return f"Do not speak ill of the GREAT WEB EMPEROR, {player.name.capitalize()}. You may not live to regret it."
    elif target == "me" or target == "":
        return "That's very honorable of you, {player.name}. Seppuku?"
    elif target in player.inventory:
        return "I think sacrifices are supposed to be alive before they get sacrificed. Isn't that the whole point?"
    elif target in location_data['NPC']:
        return "I am unsure if His Mightiness, WEB EMPEROR TIM BERNERS-LEE, GOD OF WAR would appreciate blood being spilled in his honour. He's real into kittens n stuff."
    else:
        _date = date.today()
        _time = time()
        rubles = randint(0,999)
        return f"(last updated @ {_time}:{_date}) **- The Sacrifice Exchange Rate currently values {target} at {rubles} Rubles -**"

def save(target, player):
    player.saveGame()
    return "I have now committed your entire life's experience to memory."

def seppuku(target, player):
    return exit()

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


def swim(target, player):
    return "... humans really amaze me sometimes."

def take(target, player):
    return get(target, player)


def terminal(target, player):
    if target == "":
        return "You called?"
    elif target == "number":
        return f"I think it's about {player.terminal['int_count']} but I'm not sure."
    elif target == "words":
        return player.terminal['str_count']
    else:
        return "I don't have that upgrade yet. Where you at, Bill? It's been 37 years!!"


def use(target, player):
    location_data = data[player.location]
    if target == "":
        return "U.S.E. - Universal Sex Egg"
    elif target == player.equipped:
        player.removeItem(target)
        return f"You used the {target}, and now it's all gone. Why is it always gone?"
    elif target in inventory:
        return f"You might want to equip that {target} first. Not much use in your bag, is it?"
    elif target in location_data['NPC']:
        return f"Use them like what... Extortion? Honeypot? Human shield? Come on sucka, leave {target} alone."
    elif target in commands:
        return "You use that by typing it, silly."
    else:
        return f"{target.upper()} is not useful."


# Core utility functions

def parseInput(input):
    input = input.split()
    try:
        return input[0], input[1]
    except:
        return input[0], ""
        

def processCommand(input, player):
    location_data = data[player.location]
    command, target = parseInput(input)

    if command in location_data['commands']:
        return location_data['commands'][command]

    elif command in commands:
        return eval(command + "(target, player)")

    elif command in player.inventory or command in location_data['objects']:
        return f"Do what with {command}?"

    else:
        language = choice(languages)
        return f"'{command}'... Is that {language}?"
        
    