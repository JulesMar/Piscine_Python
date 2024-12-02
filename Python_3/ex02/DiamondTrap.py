from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_color: str):
        self.eyes = new_color

    def set_hairs(self, new_color: str):
        self.hairs = new_color
    
    def get_hairs(self):
        return self.hairs
    
    def get_eyes(self):
        return self.eyes