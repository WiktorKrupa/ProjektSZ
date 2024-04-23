from Models.IComponent import Component
from Models.DeckModel import Deck
from Models.WheelsModel import Wheels
from Models.TracksModel import Tracks
from Models.PlywoodModel import Plywood
from abc import ABC, abstractmethod

#Konstruktor obiektu deskorolka
class Skateboard(Component):
    def __init__(self, bomLevel, batchSize, leadTime, inStock, quantity, wheels, tracks, deck, plywood):
        self.bomLevel= bomLevel
        self.batchSize = batchSize
        self.leadTime = leadTime
        self.inStock = inStock
        self.quantity = quantity
        self.wheels = wheels
        self.tracks = tracks
        self.deck = deck
        self.plywood = plywood


#Funkcja do testów
    def display_info(self):
        print("Skateboard Information:")
        self.wheels.display_info()
        print('\n')
        self.tracks.display_info()
        print('\n')
        self.deck.display_info()
        print('\n')
        self.plywood.display_info()
        
