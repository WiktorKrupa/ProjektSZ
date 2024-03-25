from Models.IComponent import Component
from Models.DeckModel import Deck
from Models.WheelsModel import Wheels
from Models.TracksModel import Tracks
from Models.PlywoodModel import Plywood
from abc import ABC, abstractmethod

class Skateboard(Component):
    def __init__(self, bomLevel, batchSize, leadTime, inStock, quantity, wheels, tracks, deck, plywood):
        self.bom = bomLevel
        self.batchSize = batchSize
        self.leadTime = leadTime
        self.inStock = inStock
        self.quantity = quantity
        self.wheels = wheels
        self.tracks = tracks
        self.deck = deck
        self.plywood = plywood

    def display_info(self):
        print("Skateboard Information:")
        self.wheels.display_info()
        print('\n')
        self.tracks.display_info()
        print('\n')
        self.deck.display_info()
        print('\n')
        self.plywood.display_info()
        

my_plywood = Plywood(bomLevel = 2, batchSize = 14, leadTime = 1, inStock = 4, quantity = 1)

my_wheels = Wheels(bomLevel = 1, batchSize = 20, leadTime = 2, inStock = 22, quantity = 4)  
my_tracks = Tracks(bomLevel = 1, batchSize = 10, leadTime = 3, inStock = 10, quantity = 2)
my_deck = Deck(bomLevel = 1, batchSize = 12, leadTime = 1, inStock = 13, quantity = 1) 

my_skateboard = Skateboard(bomLevel = 0, batchSize = 10, leadTime = 2, inStock = 30, quantity = 1 ,wheels = my_wheels, tracks = my_tracks, deck = my_deck, plywood = my_plywood)

my_skateboard.display_info()
