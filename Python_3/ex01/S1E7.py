from S1E9 import Character

class Baratheon(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        if self.is_alive:
            self.is_alive = False
        else:
            print(f"{self.first_name} is already dead.")


class Lannister(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        if self.is_alive:
            self.is_alive = False
        else:
            print(f"{self.first_name} is already dead.")

    def create_lannister(self, first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)
