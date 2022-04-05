import random

games = int(input("How many games?"))
# how many games they want to play

while games >0:
    computer = random.choice(["rock","paper","scissors"])
    #[] for text
    player = input("Rock, Paper or Scissors?")
    
    if player == "exit":
      break
    
    print(computer)
    
    if player == computer:
      print("It's a draw!")
      
    if player == "rock":
      if computer == "scissors":
        print("You are a Winner!")
      if computer == "paper":
        print("You've lose, try again!")
    
    if player == "paper":
      if computer == "rock":
        print("You are a Winner!")
      if computer == "scissors":
        print("You've lose, try again!")
    
    if player == "scissors":
      if computer == "paper":
        print("You are a Winner!")
      if computer == "rock":
        print("You've lose, try again!")
    
    games = games - 1 
print("See you next time!")
    
    # == means compare of two. 
