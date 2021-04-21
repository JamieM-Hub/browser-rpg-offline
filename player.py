import json

class Player:

    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
        self.equipped = "nothing"
        self.terminal_int = 0,
        self.terminal = {
            "int_count": 0,
            "str_count": ""
        }


    def changeLocation(self, new_location):
        self.location = new_location


    def changeName(self, new_name):
        print("new name: " + new_name)
        self.name = new_name


    def equipItem(self, item):
        self.equipped = item


    def saveGame(self):
        save_data = {
            "player": {
                "name": self.name,
                "location": self.location,
                "inventory": self.inventory,
                "equipped": self.equipped,
                "terminal": {
                    "int_count": self.terminal['int_count'],
                    "str_count": self.terminal['str_count']
                }
            }
        }
        with open("data/save_data.json", "w") as fp:
            json.dump(save_data, fp)
    

    def loadGame(self):
        with open("data/save_data.json", "r") as r:
            save_data = json.load(r)
        self.name = save_data['player']['name']
        self.location = save_data['player']['location']
        self.inventory = save_data['player']['inventory']
        self.equipped = save_data['player']['equipped']
        self.terminal['int_count'] = save_data['player']['terminal']['int_count']
        self.terminal['str_count'] = save_data['player']['terminal']['str_count']



class NPC:

    def __init__(self, name, location, quest):
        self.name = name
        self.location = location
        self.quest = quest
