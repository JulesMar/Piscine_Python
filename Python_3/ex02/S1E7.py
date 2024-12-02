from S1E9 import Character

class Baratheon(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Your docstring for Method"""
        if self.is_alive:
            self.is_alive = False
        else:
            print(f"{self.first_name} is already dead.")

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"{self.__str__()}>"

class Lannister(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Your docstring for Method"""
        if self.is_alive:
            self.is_alive = False
        else:
            print(f"{self.first_name} is already dead.")

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        print("create first_name : ", first_name)
        return Lannister(first_name, is_alive)
    
    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"{self.__str__()}>"
