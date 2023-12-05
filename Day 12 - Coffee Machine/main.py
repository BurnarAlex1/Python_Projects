import coffee
import coffee_machine

latte=coffee.Coffee('latte',150,100,50,2.00)
cappucino=coffee.Coffee('cappucino',200,150,100,3.50)
espresso=coffee.Coffee('espresso',100,0,50,1.50)


machine=coffee_machine.CoffeeMachine()

while True:
    option=input("Do you want to use the machine?(Y/N)")
    if option=='N':
        break
    print("Good morning!")
    option=input("What would you like to purchase?(espresso,latte,cappucino)")

    if option=='administration':
        print('You are in admin mode.')
        option=input('Would you like to supply more water,milk or beans?')
        amount=int(input("Give the amount you want to give:"))
        if option=='milk':
            machine.supply_milk(amount)
        elif option=='water':
            machine.supply_water(amount)
        elif option=='beans':
            machine.supply_beans(amount)

    elif option=='status':
        print("The machine currently has "+str(machine.coffee_beans) +' gr of beans')
        print("The machine currently has " + str(machine.milk) + ' ml of milk')
        print("The machine currently has " + str(machine.water) + ' ml of water')

    elif option=='espresso':
        if machine.check_resources(espresso) == True:
            quarters=float(input("Give the number of quarters: "))
            dimes = float(input("Give the number of dimes: "))
            nickels = float(input("Give the number of nickels: "))
            pennys=float(input("Give the number of pennys: "))
            if machine.count_money(quarters,dimes,nickels,pennys,espresso)==True:
                machine.purchase_coffee(espresso)

    elif option=='latte':
        if machine.check_resources(latte) == True:
            quarters=float(input("Give the number of quarters: "))
            dimes = float(input("Give the number of dimes: "))
            nickels = float(input("Give the number of nickels: "))
            pennys=float(input("Give the number of pennys: "))
            if machine.count_money(quarters,dimes,nickels,pennys,latte)==True:
                machine.purchase_coffee(latte)

    elif option=='cappucino':
        if machine.check_resources(latte) == True:
            quarters=input("Give the number of quarters: ")
            dimes = input("Give the number of dimes: ")
            nickels = input("Give the number of nickels: ")
            pennys=input("Give the number of pennys: ")
            if machine.count_money(quarters,dimes,nickels,pennys,cappucino)==True:
                machine.purchase_coffee(cappucino)



