"""

Inputs:
A string containing an attribute guess or the guess of the animal's name.

Processes:
- Randomly select an animal.
- Allow the user to guess until they guess the correct animal.
- When they guess, tell them if the animal has the attribute or not.
- Tell the user when the guess correctly.

Outputs:
- Attribute guess correctness
- Congratulations message

"""

import random       # Teach Python how to do random stuff

ANIMALS = {
    "Lion" : ["Mammal", "Claws", "Yellow", "Predator", "Africa", "Carnivore", "Four legs", "Cat", "Fur"],
    "Hyena" : ["Mammal", "Claws", "Yellow", "Spots", "Predator", "Africa", "Carnivore", "Four legs", "Scavenger", "Fur"],
    "Panther" : ["Mammal", "Claws", "Black", "Spots", "Predator", "Jungle", "Carnivore", "Four legs", "Climbs trees", "Cat", "Fur"],
    "Eagle" : ["Bird", "Two legs", "Wings", "Predator", "Carnivore", "Flies", "Talons", "Solitary", "Feathers"],
    "Pigeon" : ["Bird", "Two legs", "Wings", "Scavenger", "Omnivore", "Flies", "Flock", "Gray", "Feathers"],
    "Chicken" : ["Bird", "Two legs", "Wings", "Scavenger", "Omnivore", "Flocks", "Feathers"],
    "Human" : ["Mammal", "Fingers", "Omnivores", "Two legs", "Fur"],
    "Turtle" : ["Amphibean", "Four legs", "Omnivore", "Green", "Swim", "Shell", "Bite"]
}

WELCOME_MESSAGE = """Animal guessing game
I have picked a random animal. Guess an
attribute or the name of the animal.
"""

CONGRATUALTIONS_MESSAGE = "You won!"


list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]

print(WELCOME_MESSAGE)

guess = ""

while guess != random_animal:
    guess = input("Please guess an attribute or an animal name: ").capitalize()
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATUALTIONS_MESSAGE)
    elif guess == "Exit":
        break
    else:
        print(f"No, {guess} is NOT an attribute of the animal.")
