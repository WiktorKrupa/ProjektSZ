from Models.IComponent import Component

class Wheels(Component):
    #Klasa dziedzicząca po interface IComponent
    
    
    #Funkcja do testów
    def display_info(self):
        print("Wheels Information:")
        print(f"BOM Level: {self.bom}")
        print(f"Batch Size: {self.batchSize}")
        print(f"Lead Time: {self.leadTime}")
        print(f"In stock: {self.inStock}")
        print(f"Quantity needed: {self.quantity}")