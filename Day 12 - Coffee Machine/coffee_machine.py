

class CoffeeMachine:
    def __init__(self):
        self.water=0
        self.milk=0
        self.coffee_beans=0

    def supply_water(self,water):
        self.water=self.water+water

    def supply_milk(self,milk):
        self.milk=self.milk+milk

    def supply_beans(self,beans):
        self.coffee_beans=self.coffee_beans+beans

    def purchase_coffee(self,coffee):
        self.water=self.water-coffee.water
        self.milk = self.milk - coffee.milk
        self.coffee_beans = self.coffee_beans - coffee.coffee_beans

    def count_money(self,quarter,dime,nickel,penny,coffee):
        money=quarter*0.25+dime*0.10+nickel*0.05+penny*0.01
        if money<coffee.price:
            print("Not enough coins were added! Everything has been refunded!")
            return False
        elif money==coffee.price:
            print("The exact sum has been added and no change is needed!")
            print("Here is your "+coffee.name+'! Have a good day!')
            return True
        else:
            change=money-coffee.price
            print("The change after the tranzaction is "+str(change)+'$')
            print("Here is your " + coffee.name + '! Have a good day!')
            return True

    def check_resources(self,coffee):
        if self.milk<coffee.milk:
            print('There isnt enough milk!')
            return False
        elif self.coffee_beans<coffee.coffee_beans:
            print("There arent enough coffee beans!")
            return False
        elif self.water<coffee.water:
            print('There is not enough water!')
            return False
        else:
            return True
