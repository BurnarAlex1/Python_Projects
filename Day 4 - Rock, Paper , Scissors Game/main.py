import random

print("Welcome to the Rock, Paper, Scissors Game!")
option=input("Choose to play Rock , Paper or Scissors(0,1 or 2)")
if(option=='0'):
  
  print('You choose Rock')
  # Rock
  print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)
elif(option=='1'):
  print('You choose Paper')
  
  # Paper
  print("""
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  """)
elif(option=='2'):
  print('You choose Scissors')
  
  # Scissors
  print("""
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)
else:
  print('You need to choose 0,1 or 2')

computer_option= random.randint(0,2)
if(computer_option==0):

  print('The computer choose Rock')
  # Rock
  print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)
elif(computer_option==1):
  print('The computer choose Paper')

  # Paper
  print("""
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  """)
elif(computer_option==2):
  print('The computer choose Scissors')

  # Scissors
  print("""
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)

if(option==str(computer_option)):
  print('There is a tie!')
elif(option=='0'):
  if(computer_option==1):
    print('You lose!')
  else:
    print('You win!')
elif(option=='1'):
  if(computer_option==0):
    print('You win!')
  else:
    print('You lose!')
elif(option=='2'):
  if(computer_option==0):
    print('You lose!')
  else:
    print('You win!')

