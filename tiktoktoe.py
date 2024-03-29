#!/usr/bin/env python

# tiktoktoes

import os
import requests
import random

bored = ["-"] * 9
player = "X"

def print_intro():
    print("Welcome, gyats and rizzlers, to TikTokToes!")
    print(" ")
    print("If you get three in a row, you win a feet pic!")
    print(" ")
    input("Keep looksmaxxing and press Enter to start...")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_board(bored):
  print(f" {bored[0]} | {bored[1]} | {bored[2]} ")
  print("-----------")
  print(f" {bored[3]} | {bored[4]} | {bored[5]} ")
  print("-----------")
  print(f" {bored[6]} | {bored[7]} | {bored[8]} ")

def player_input(bored):
  move = int(input().strip())
  while bored[move-1] != "-":
    print("You got fanum taxed, try again.")
    move = int(input().strip())
  return move

def check_win(bored):
    win_positions = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],
      [0, 3, 6], [1, 4, 7], [2, 5, 8],
      [0, 4, 8], [2, 4, 6]
    ]
    for win_pos in win_positions:
        if all(bored[pos] == player for pos in win_pos):
          return True
    return False

def feetpic(url, filename):
  response = requests.get(url)
  with open(filename, 'wb') as f:
    f.write(response.content)

def switch_player(current_player):
  return "O" if current_player == "X" else "X"

def main():
  global player
  print_intro()
  clear()
  print_board(bored)
  while True:
      print("Rizz them up 1-9 ")
      move = player_input(bored)
      bored[move-1] = player
      clear()
      print_board(bored)
      print("Current player: " + player)
      if check_win(bored):
        print_board(bored)
        clear()
        print("You got three in a row you absolute sigma.")
        print(" ")
        print("A feetpic was just dropped on your desktop.")
        urls = [
          "https://github.com/fenette/feetpics/blob/main/pics/cutefeet.jpg?raw=true",
          "https://github.com/fenette/feetpics/blob/main/pics/fancyfeet.jpg?raw=true",
          "https://github.com/fenette/feetpics/blob/main/pics/lovelyfoot.jpg?raw=true",
          "https://github.com/fenette/feetpics/blob/main/pics/sexyfoot.jpg?raw=true",
          "https://github.com/fenette/feetpics/blob/main/pics/sophisticatedfeet.jpg?raw=true"
        ]
        selected_url = random.choice(urls)
        feetpic(selected_url, "feetpic.jpg")
        break
      if all(pos != "-" for pos in bored):
        print("It's a tie. Skibidi. ")
        break
      player = switch_player(player)

if __name__ == "__main__":
    main()









