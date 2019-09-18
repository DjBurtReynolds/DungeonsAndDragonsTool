import random

basic_player_classes = ("Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard")

player_races = ("Aarakocra", "Aasimar", "Bugbear", "Centaur","Changeling", "Dragonborn", "Dwarf",  "Elf", "Firbolg", "Goblin","Genasi", "Gith", "Gnome", "Goliath", "Half-Elf", "Halfling", "Half-Orc", "Hobgoblin","Human", "Kalashtar", "Kenku", "Kobold", "Lizardfolk", "Loxodon", "Minotaur","Orc", "Simic Hybrid", "Shifter", "Tabaxi","Tiefling", "Tortle", "Triton", "Vedalken", "Verdan","Warforged", "Yuan-ti Pureblood")

def main_menu():
	 print("===========Main Menu===========\n1.Random Character Generator\n2.Dice Roller\n3.Character Creation")
	 choice = input().lower()
	 if choice == "1":
	 	return random_character()
	 if choice == "2":
	 	return dice_roller()
	 if choice == "exit":
	 	return 
	 return main_menu()
def random_character():
	random_class =  basic_player_classes[random.randint(0,11)]
	random_race = player_races[random.randint(0,36)]
	print(f"Your race is {random_race} and your class is {random_class}")
	return main_menu()
def d4():
	return random.randint(1,4)

def d6():
	return random.randint(1,6)

def d8():
	return random.randint(1,8)

def d10():
	return random.randint(1,10)

def d12():
	return random.randint(1,12)

def d20():
	return random.randint(1,20)

def dice_roller():
	answer = ""
	while answer != "done":      #Repeats dice roller until done is typed
		answer = input("===========Dice Roller===========\n     1.D20            4.D8\n     2.D12            5.D6\n     3.D10            6.D4\n\n\n").lower()
		print("\n\n\n")
		if answer == "1":
			print("You rolled a " + str(random.randint(1,20)))
		elif answer == "2":
			print("You rolled a " + str(random.randint(1,12)))
		elif answer == "3":
			print("You rolled a " + str(random.randint(1,10)))
		elif answer == "4":
			print("You rolled a " + str(random.randint(1,8)))
		elif answer == "5":
			print("You rolled a " + str(random.randint(1,6)))
		elif answer == "6":
			print("You rolled a " + str(random.randint(1,4)))
	return main_menu()

main_menu()
