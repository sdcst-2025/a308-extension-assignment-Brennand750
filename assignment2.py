'''Task 2'''
import random
wincount = 0
incorrectcount = 0
playagain = 'yes'
while playagain == 'yes':
    playerchoice = input("Please enter your choice of either heads or tails")
    cointoss = random.choice(['heads','tails'])
    print(f"The coin landed on", {cointoss})
    if cointoss == playerchoice:
        print("Congrats you win!")
        wincount =+ 1
    else:
        print("You lose, do you want to play again")
        incorrectcount =+ 1
        playagain = input("Do you want to play again?")
        if playagain not in ("yes", "y"):
            print("Thanks for playing")
        


print(f"The amount of times you got it correct", {wincount})
print(f"The amount of times you got it incorrect", {incorrectcount})




