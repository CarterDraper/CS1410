import random
import sys
import os

# Function to clear the terminal screen based on the OS
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')

#TODO: If you are on a computer other than a mac, replace os.system('clear') with os.system('cls')
#TODO: Print the following to the console:
#   "What is your name, adventurer?"
#TODO: Have the user input their name and then print:
#   "Welcome, <player>, to Simple RPG!"
msg = "What is your name, adventurer?"
print(msg)
name = input("")
print(f"Welcome, {name}, to Simple RPG!")

adventureClass = input("Choose your class: (1) Barbarian, (2) Knight, (3) Rogue: ")

#TODO: Write a series of if statements to set the stats of the player's chosen class
#   The stats should be the following:
#   If a Barbarian:
#       players max health = 75
#       maximum damage dealt = 20
#       player speed = 8
#       maximum heal rate = 10
if adventureClass == "1":
    playerhealth = 75
    damage = 20
    speed = 8
    healrate = 10

#   If a Knight:
#       players max health = 60
#       maximum damage dealt = 15
#       player speed = 5
#       maximum heal rate = 15
elif adventureClass == "2":
    playerhealth = 60
    damage = 15
    speed = 5
    healrate = 15
#   If a Rogue:
#       players max health = 50
#       maximum damage dealt = 10
#       player speed = 3
#       maximum heal rate = 20
elif adventureClass == "3":
    playerhealth = 50
    damage = 10
    speed = 3
    healrate = 20
#   Please remember to create logic that does not allow the player to input
#   anything other than 1,2, or 3
else:
    print("Invalid class choice. Exiting...")
    sys.exit()

healthMax = playerhealth
health = healthMax

fightCnt = 0
runFlg = 0
fearFlg = 0
attackRoll = 0
guardRoll = 0
runRoll = 0
enemySpecRoll = 0

while fightCnt < 5:
    #TODO: Inside of random.choice(), create a list with the following items:
    #   "Sewer Rat", "Skeleton", "Zombie"
    enemyChoice = random.choice(["Sewer Rat", "Skeleton", "Zombie"])
    if enemyChoice == "Sewer Rat":
        enemyHealth = 25
        enemyDamage = 5
        enemySpeed = 3
        enemySpecial = "poison"
        enemyWeakness = "Rogue"
    elif enemyChoice == "Skeleton":
        enemyHealth = 35
        enemyDamage = 10
        enemySpeed = 5
        enemySpecial = "fear"
        enemyWeakness = "Cleric"
    elif enemyChoice == "Zombie":
        enemyHealth = 40
        enemyDamage = 12
        enemySpeed = 8
        enemySpecial = "heal"
        enemyWeakness = "Barbarian"

    clear_screen()
    print("You have encountered a " + enemyChoice + "!")
    print("Enemy Health: " + str(enemyHealth))
    escapedFlg = 0

    while enemyHealth > 0 and health > 0 and escapedFlg == 0:
        # Player Turn
        print("Your Turn: ")
        print("Player Health: " + str(health))
        while True and fearFlg == 0:
            playerChoice = input("(1) Attack, (2) Guard, (3) Run Away: ")
            clear_screen()
            if playerChoice == "1":
                attackRoll = random.randint(1, 20)
                #TODO: program the player attack logic. To do so, start by
                #   checking if attackRoll is less than the speed variable
                #   if it is, set attackRoll = 0
                #   otherwise, set attackRoll to be a random integer between 1 and
                #   the damage variable. HINT: use the random.randint() function
                #TODO: if attackRoll is greater than 0, tell the player how much they
                #   hit the enemy for, otherwise tell the player that they missed
                if attackRoll < speed:
                    attackRoll = 0
                else:
                    attackRoll = random.randint(1, damage)
                if attackRoll > 0:
                    enemyHealth -= attackRoll
                    print(f"You hit the enemy for {attackRoll} points!")
                else:
                    print("You missed!")

            elif playerChoice == "2":
                #TODO: program the player guard logic. To do so, start by
                #   setting guardRoll = a random number between 1 and the healRate variable
                #   add guardRoll to the health variable
                #   remember to tell the player how much they healed for
                guardRoll = random.randint(1, healrate)
                health += guardRoll
                if health > healthMax:
                    health = healthMax
                print(f"You guarded and healed for {guardRoll} points!")
            elif playerChoice == "3":
                #TODO: program the player run logic
                runRoll = random.randint(1, 20)
                if runRoll >= 12:
                    print("You have successfully run away")
                    if health < healthMax:
                        health += (healthMax // 2)
                        if health > healthMax:
                            health = healthMax
                    print("Your health has been restored to " + str(health))
                    escapedFlg = 1
                else:
                    print("You have failed to run away")
                break
            else:
                print("Invalid input, please enter a valid number")
        
        if escapedFlg == 0:
            if adventureClass == "1" and enemyChoice == "Zombie":
                enemyHealth -= 2
                print("You dealt 2 points of bonus damage!")
            elif adventureClass == "2" and enemyChoice == "Skeleton":
                enemyHealth -= 2
                print("You dealt 2 points of bonus damage!")
            elif adventureClass == "3" and enemyChoice == "Sewer Rat":
                enemyHealth -= 2
                print("You dealt 2 points of bonus damage!")

        if enemyHealth <= 0:
            print("You have killed the " + enemyChoice)
            break

        # Enemy Turn
        clear_screen()
        fearFlg = 0
        print(enemyChoice + "'s Turn: ")
        print("Enemy Health: " + str(enemyHealth))

        #TODO: set attackRoll to be a random integer between 1 and 20
        #   next, check if attackRoll is less than enemySpeed. If it is
        #   set attackRoll = 0 otherwise set it to be a random number
        #   between 1 and the variable named enemyDamage
        #   finally, subtract attackRoll from the health variable
        attackRoll = random.randint(1, 20)
        if attackRoll < enemySpeed:
            attackRoll = 0
        else:
            attackRoll = random.randint(1, enemyDamage)
        health -= attackRoll

        if health <= 0:
            print("You Died! Game Over!")
            sys.exit()

        print("The enemy dealt " + str(attackRoll) + " points of damage")

        specialRoll = random.randint(1, 20)
        if specialRoll >= 15:
            if enemyChoice == "Sewer Rat":
                print("The enemy has poisoned you! 2 points of damage!")
                health -= 2
            elif enemyChoice == "Skeleton":
                print("The enemy has frightened you! Lose your next turn!")
                fearFlg = 1
            elif enemyChoice == "Zombie":
                print("The enemy has found its missing limb! It has healed to 5 points!")
                enemyHealth += 5
                if enemyHealth > 40:
                    enemyHealth = 40
        
    fightCnt += 1

print("You have cleared the dungeon! You win!")
