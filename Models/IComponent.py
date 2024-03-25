from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, bomLevel, batchSize, leadTime, inStock, quantity):
        self.bom = bomLevel
        self.batchSize = batchSize
        self.leadTime = leadTime
        self.inStock = inStock
        self.quantity = quantity
    
    @abstractmethod
    def display_info(self):
        pass