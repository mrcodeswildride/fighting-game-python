import os
import random

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  print("--------------------")
  print(f"Your HP: {player_hp}")
  print(f"Computer HP: {computer_hp}")
  print("--------------------\n")

def get_player_move():
  while True:
    move = input("Choose [a]ttack, [d]efend, or [h]eal: ").lower()

    if move in ["a", "attack"]:
      return "attack"
    elif move in ["d", "defend"]:
      return "defend"
    elif move in ["h", "heal"]:
      return "heal"
    else:
      print("Invalid move.\n")

def get_attack_points():
  return random.randint(10, 20)

def get_defense_points(attack_points):
  return attack_points // 2, int(attack_points * 0.2)

def get_healing_points():
  return random.randint(5, 12)

player_hp = 100
computer_hp = 100

while player_hp > 0 and computer_hp > 0:
  print_game_state()

  player_move = get_player_move()
  computer_move = random.choice(["attack", "defend", "heal"])
  print()

  if player_move == "attack":
    if computer_move == "attack":
      player_damage = get_attack_points()
      computer_damage = get_attack_points()
      player_hp -= computer_damage
      computer_hp -= player_damage
      print(f"You attacked for {player_damage} points, and computer attacked for {computer_damage} points.")
    elif computer_move == "defend":
      player_damage_initial = get_attack_points()
      computer_damage, player_damage = get_defense_points(player_damage_initial)
      player_hp -= computer_damage
      computer_hp -= player_damage
      print(f"You attacked for {player_damage_initial} points, but computer defended, taking {player_damage} points and dealing {computer_damage} points of recoil.")
    elif computer_move == "heal":
      player_damage = get_attack_points()
      computer_heal = get_healing_points()
      computer_hp -= (player_damage - computer_heal)
      print(f"You attacked for {player_damage} points, and computer healed for {computer_heal} points.")
  elif player_move == "defend":
    if computer_move == "attack":
      computer_damage_initial = get_attack_points()
      player_damage, computer_damage = get_defense_points(computer_damage_initial)
      player_hp -= computer_damage
      computer_hp -= player_damage
      print(f"Computer attacked for {computer_damage_initial} points, but you defended, taking {computer_damage} points and dealing {player_damage} points of recoil.")
    elif computer_move == "defend":
      print("You and computer both defended. Nothing happened.")
    elif computer_move == "heal":
      computer_heal = get_healing_points()
      computer_hp += computer_heal
      print(f"You defended, and computer healed for {computer_heal} points.")
  elif player_move == "heal":
    if computer_move == "attack":
      player_heal = get_healing_points()
      computer_damage = get_attack_points()
      player_hp -= (computer_damage - player_heal)
      print(f"Computer attacked for {computer_damage} points, and you healed for {player_heal} points.")
    elif computer_move == "defend":
      player_heal = get_healing_points()
      player_hp += player_heal
      print(f"Computer defended, and you healed for {player_heal} points.")
    elif computer_move == "heal":
      player_heal = get_healing_points()
      computer_heal = get_healing_points()
      player_hp += player_heal
      computer_hp += computer_heal
      print(f"You healed for {player_heal} points, and computer healed for {computer_heal} points.")

  player_hp = max(min(player_hp, 100), 0)
  computer_hp = max(min(computer_hp, 100), 0)

  input("\nPress enter to continue. ")

print_game_state()

if player_hp == 0 and computer_hp == 0:
  print("Nobody wins")
elif player_hp == 0:
  print("Computer wins!")
else:
  print("You win!")
