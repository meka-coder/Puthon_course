class Hero :

    def __init__(self, name,helth,power):
        self.name = name
        self.__helth = helth
        self.power = power

    def attack(self):
        return f"the fight {self.name} attacks with power {self.power}!"   

    def get__helth(self):

        return self.__helth

    def set__helth(self,new_helth):

        if self.__helth < 0 :
            
            self.__helth = 0
            return f"The hero is dead!"
        else:
            return self.__helth = new_helth    

    def __str__(self):
        return f"my hero {self.name} .your power is { self.power} " 

   # def __gt__(self):



class Mage (Hero):

    def __init__(self,name,helth,power,mana):
        super().__init__(name,helth,power)
        self.mana=mana

    def attack(self):
        return f"The Mage {self.name} casts a spell using mana!."     





