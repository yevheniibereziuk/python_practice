class Hero():
    """Class to create hero for our project"""

    def __init__(self, name, level, race):
        """Initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.healf = 100


    def show_hero(self):
        """Print all parameters of this Hero"""
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health " + str(self.healf)).title()
        print(description)
    

    def level_up(self):
        """Upgrade lvl of hero"""
        self.level += 1
    
    def move(self):
        """Start moving Hero"""
        print("Hero " + self.name + " start moving... ")

    def set_health(self, new_health):
        self.healf = new_health


class SuperHero(Hero):
    """Class to create super Heroo"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100
    
    def makemagic(self):
        """Use magic"""
        self.magic -= 10
    
    def show_hero(self):
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health " + str(self.healf) + " Magic is: " + str(self.magic)).title()
        print(description)
