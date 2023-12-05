print('Welcome to Treasure Island\nYour objective is to find the treasure.')
print("\n\nYour are sitting at the cross roads, there are two paths in front of you. Choose the path you want to take(Left or Right)")
option=input("")
if(option=='Left'):
  print("You take the left path and reach a lake.")
  print("You can wait for a boat to come and take you across or you can attempt to swim across.")
  print("What is your next action?(Swim or Wait")
  option=input('')
  if(option=='Wait'):
    print("A boat arrives and takes you across the lake.")
    print("You see 3 doors in front of you, a blue, red and green door.")
    print("What door do you take?(Red,Green or Blue)")
    option=input('')
    if(option=='Green'):
      print("You found the treasure, congratsulations!")
    elif(option=='Red'):
      print('You find hungry beasts and are eatten alive!')
    else:
      print("You fell into a burning fire and are consumed by flames!")
      
  else:
    print("You try to swim across but you are attacked by a crocodile and eatten!")
else:
  print('The road leads you into a dark forest and you get lost without the posibility to escape!')
