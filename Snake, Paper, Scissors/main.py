import random
import time
from symbol import rock,paper,scissors

signs=[rock,paper,scissors]
sign_names=["rock","paper","scissors"]

while(True):
  user_input=int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors: \n"))
  computer_choice=random.randint(0,2)
  # print(computer_choice)
  try:
    print(signs[user_input])
    print(f"You chose {sign_names[user_input]}")
    time.sleep(1.5)
    print(signs[computer_choice])
    print(f"Computer chose {sign_names[computer_choice]}\n")
  except:
    print("Not a good input")
  
  
  time.sleep(1.5)
  if(user_input>2 or user_input<0):
    print("Invalid Input by User\nComputer Wins!")
    
  elif(user_input==0 and computer_choice==2):
    print("User Wins!\n")
  
  elif(user_input==2 and computer_choice==0):
    print("Computer Wins!\n")
  
  elif(user_input<computer_choice):
    print("Computer Wins!\n")
    
  elif(user_input>computer_choice):
    print("User Wins!\n")
    
  elif(user_input==computer_choice):
    print("It's a draw");
  print("\n")
  print("***************************************************")
  
  time.sleep(3)
  print("\n\n")
