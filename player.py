from json import JSONEncoder
import json

class Player:
    name = "Default Dave"
    location = "l1"
    inventory = []
    equipped = "nothing"

    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
        self.equipped = "nothing"

    def changeLocation(self, new_location):
        self.location = new_location

    def equipItem(self, item):
        self.equipped = item
    
    def startCall():
        pass

    def endCall():
        pass

# A specialised JSONEncoder that encodes player objects as JSON
# https://pythontic.com/serialization/json/introduction

class playerEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Player):
          return object.__dict__
        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)

class NPC:
    def __init__(self, name, location, quest):
        self.name = name
        self.location = location
        self.quest = quest
