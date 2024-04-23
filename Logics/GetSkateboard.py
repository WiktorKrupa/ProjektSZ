from Models.SkateboardModel import Skateboard
from Models.WheelsModel import Wheels
from Models.TracksModel import Tracks
from Models.DeckModel import Deck
from Models.PlywoodModel import Plywood

#Funkcja tworząca obiekty i przypisująca im wartości 
def getSkate():
    my_plywood = Plywood(bomLevel = 2, batchSize = 14, leadTime = 1, inStock = 4, quantity = 1)

    my_wheels = Wheels(bomLevel = 1, batchSize = 20, leadTime = 2, inStock = 22, quantity = 4)  
    my_tracks = Tracks(bomLevel = 1, batchSize = 10, leadTime = 3, inStock = 10, quantity = 2)
    my_deck = Deck(bomLevel = 1, batchSize = 12, leadTime = 1, inStock = 13, quantity = 1) 

    my_skateboard = Skateboard(bomLevel = 0, batchSize = 10, leadTime = 2, inStock = 30, quantity = 1 ,
                               wheels = my_wheels, tracks = my_tracks, deck = my_deck, plywood = my_plywood)
    
    
    #Zwrócenie obiektu klasy Skateboard z atrybutami
    return my_skateboard