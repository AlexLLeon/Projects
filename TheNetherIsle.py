# What do you want to be known by?

def player_intro():
    print("Welcome to The Nether Isle!")

    player = input(str("What is your name, adventurer? \n"))
    print(f"Ah good to meet you, {player}.")
  
    character_class = get_class()
    print(f"{character_class} is a mighty fine choice!")

    weapon = get_weapon()

    print (f"So you're a {weapon} wielding {character_class}! Welcome to the Nether Isle, {player}.")
 

# What class?

def get_class():
    res = input(str("What class are you, traveller? \n[1] Barbarian \n[2] Wizard \n[3] Rogue \n[4] Ranger \n"))

    if res == "1":
        return "Barbarian"
    elif res == "2":
        return "Wizard"
    elif res == "3":
        return "Rogue"
    elif res == "4":
        return "Ranger"
    else:
        return "Sorry, I didn't understand your input. Please respond with 1, 2, 3 or 4."

      
# What weaapon?
      
def get_weapon():
    res = input(str("What weapon will you be using? \n[1] Sword \n[2] Axe \n[3] Staff \n[4] Bow \n[5] Dagger \n[6] Crossbow \n"))

    if res == "1":
        return "Sword"
    elif res == "2":
        return "Axe"
    elif res == "3":
        return "Staff"
    elif res == "4":
        return "Bow"
    elif res == "5":
        return "Dagger"
    elif res == "6":
        return "Crossbow"
    else:
        return "Sorry, I didn't understand your input. Please respond with 1, 2, 3, 4, 5 or 6."
    

player_intro()
