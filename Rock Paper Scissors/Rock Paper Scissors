import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

while True:
  import random
  #players choice 
  player_choice = input("Rock Paper or Scissors? ")
  
  if player_choice not in ["rock","paper","scissors"]:
    print('Please re-enter!')
    continue
    
  if player_choice == "exit":
    break

  print(player_choice)
  
  #computers choice
  computer_choice = random.choice(["rock", "paper", "scissors"])
  print(computer_choice)
  #draw outcome 
  #if the player's choice matches the computer's choice
    #it's a draw
  if player_choice == computer_choice:
    print("It's a draw!")
  
      
      
  #win outcome 
  if player_choice == "rock":
    if computer_choice == "scissors":
      print("You've won!")
      
  if player_choice == "paper":
    if computer_choice == "rock":
      print("You've won!")
      
  if player_choice == "scissors":
    if computer_choice == "paper":
      print("You've won!")
    #player wins 
  
  
  #lose outcome
  if player_choice == "rock":
    if computer_choice == "paper":
      print("You've lost!")
      
  if player_choice == "paper":
    if computer_choice == "scissors":
      print("You've lost!")
      
  if player_choice == "scissors":
    if computer_choice == "rock":
      print("You've lost!")
    #player loses 
