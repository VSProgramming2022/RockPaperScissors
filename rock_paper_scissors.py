import random

def main():
  while True:
    comp_choice = random.choice(["R", "P", "S"])
    user_choice = input("[R]ock [P]aper [S]cissor >> ").upper()

    if user_choice == "R" and comp_choice == "S":
      print("You Win!")

    elif user_choice == "S" and comp_choice == "P":
      print("You Win!")

    elif user_choice == "P" and comp_choice == "R":
      print("You Win!")

    elif comp_choice == "R" and user_choice == "S":
      print("You Lost!")

    elif comp_choice == "S" and user_choice == "P":
      print("You Lost!")

    elif comp_choice == "P" and user_choice == "R":
      print("You Lost!")

    elif comp_choice == user_choice:
      print("Draw!")

    if user_choice == "E":
      break

    print("You: " + user_choice + " Comp: " + comp_choice)

if __name__ == '__main__':
  main()