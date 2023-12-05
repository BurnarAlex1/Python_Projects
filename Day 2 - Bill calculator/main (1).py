print("Welcome to the tip calculator")
price = float(input("What is the price you need to pay?\n"))
tip_percentage= int(input("What is the tip percentaje you want to give?(0,10,15\n"))
nr_of_people = int(input("How many people are splitting the bill?\n"))
if tip_percentage==0 or tip_percentage==10 or tip_percentage==15:
  price=(((price*tip_percentage)/100)+price)/nr_of_people
  print("The price is " + str(price)+'$')
  
