from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Deadlock Characters")
table.add_column("Name", style="cyan", no_wrap=False)
table.add_column("Ability 1", style="green", no_wrap=False)
table.add_column("Ability 2", style="red", no_wrap=False)
table.add_column("Ability 3", style="yellow", no_wrap=False)
table.add_column("Ability 4", style=" magenta", no_wrap=False)

table.add_row("Bebop", "Exploding Uppercut", "Sticky Bomb", "Hook", "Hyperbeam")
table.add_row("The Doorman", "Call Bell", "Doorway", "Luggage Cart", "Hotel Guest")
table.add_row("Mina", "Rake", "Sanguine Retreat", "Love Bites", "Nox Nostra")

# console.print(table)
console.print("\n[bold cyan]Now I want you to enter your own character![/bold cyan]")

# with open("python-libraries/heroes.csv", "wt", encoding="utf-8") as outfile:
#     csvout = csv.writer(outfile, '')

def add_char():
    chars = [] # Will contain all characters added
    scratch = [] # This is a list that will get rewritten
    heroes_added = input("Enter the amount of heroes you want to add: ")
    file = "python-libraries/heroes.csv" # This contains the file path, it's helpful for writing to a csv and printing later
    for i in range(int(heroes_added)): # Establishes how many times this loop repeats.
        name = input("Enter the name of your character: ")
        scratch.append(name)
        for i in range(4): # Deadlock characters have 4 abilities
            ability = input("Enter Ability " + str(i + 1) + ": ")
            scratch.append(ability) # adding all the abilities to our "scratch" list 
        print(scratch)
        correct = input("Is this the correct data? ") # Confirming with the user
        if correct.lower() == "yes":
            chars.append(scratch)
            # csvout.writerow(chars)
            with open(file, "w") as outfile: # Writing out the final file
                for char in chars:
                    outfile.write(str(char)) + "\n"
            for name, ability_1, ability_2, ability_3, ability_4 in chars: # Adding everyting in the list to the table
                table.add_row(name, ability_1, ability_2, ability_3, ability_4)
        elif correct.lower() == "no": # Repeats the initial input loop if the user wants
            print("Please Re-enter your hero's details")
            name = input("Enter the name of your character: ")
            for i in range(4):
                ability = input("Enter Ability " + str(i + 1) + ": ")
                scratch.append(ability)
        else:
            input("Input not understood, please enter Yes or No")
        scratch = []
    console.print(table) # Prints table
    print("Your data has been added. \nYou can find it at " + file) # Prints confirmation and the file path

add_char() # function call so I can test everything
