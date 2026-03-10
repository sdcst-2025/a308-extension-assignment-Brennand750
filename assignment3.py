'''Task 4'''
import random
charactercount = 1
repeat = "yes"
while repeat == "yes":
    abilities = ["strenght", "intelligence", "wisdom", "dexterity", "constitution", "charsima"]
    scores = {}

    for ability in abilities:
        rolls =[random.randint(1,6) for _ in range(3)]
        scores[ability] = sum(rolls)

    print(f"Charcter {charactercount} Stats")
    for ability, score in scores.items():
        print(f"{ability}, {score}")
    charactercount += 1

    repeat = input("Do you want to make another DnD character")
    if repeat not in ["yes", "y"]:
        print("Thanks for playing!")



