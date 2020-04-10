from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def cook(self):
        pass

class Inventory():
    #Singleton Design Pattern 
    x = None
    def instance():
        if Inventory.x is None:
            Inventory()
        return Inventory.x
    def __init__(self):
        if Inventory.x != None:
            raise Exception
        else:
            Inventory.x = self
            
class Premade(Product):
    name = "Cheese pizza"
    def cook(self):
        print("Your pizza is being prepared: "+self.name)

class Drink(Product):
    name = "Coke Zero"
    def cook(self):
        print("Your pop is being prepared: "+self.name)

class Pasta(Product):
    name = "Spaghetti and Meatballs"
    def cook(self):
        print("Your pasta is being prepared : "+self.name)
        
class Creation(Product):
    name = "Pizza Creation"
    def cook(self):
        print("Your own Pizza creation is prepared:" +self.name)
        
class Pizza(object):
    #Builder Design Pattern

    class PizzaBuilder(object):
        
        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)

    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese
        
class Factory(ABC):
    #Factory Design Pattern

    @abstractmethod
    def get_dish(type_of_meal):
        pass

class PizzaFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "Pre-made":
            return Premade()
        if type_of_meal == "Make your Own":
            return Creation()

    def create_food(self):
        return Creation()

class MiscDishFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "Pasta":
            return Pasta()

        if type_of_meal == "Drink":
            return Drink()

class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "Type of Pizza":
            return PizzaFactory
        if type_of_factory == "Other":
            return MiscDishFactory
        
fp = FactoryProducer()

fac = fp.get_factory("Type of Pizza")
preMade = fac.get_dish("Pre-made")
preMade.cook()
creation = fac.get_dish("Make your Own")
creation.cook()

fac1 = fp.get_factory("Other")
pasta = fac1.get_dish("Pasta")
pasta.cook()
drink = fac1.get_dish("Drink")
drink.cook()


def main():
    print ("Building a pizza...")

    pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()

    if pizza.garlic:
        print ("The pizza has garlic.")
    if pizza.extra_cheese:
        print ("The pizza has extra cheese.")
  
    i = Inventory()
    i = Inventory.instance()

if __name__ == "__main__":
    main()
