import random

animals = {
    "lion": [
        "I am called the king of the jungle",
        "I am a carnivore",
        "I roar loudly"
    ],
    "elephant": [
        "I am the largest land animal",
        "I have a trunk",
        "I have tusks"
    ],
    "tiger": [
        "I have black stripes",
        "I am a carnivore",
        "I am a wild cat"
    ],
    "monkey": [
        "I love bananas",
        "I can climb trees",
        "I am very playful"
    ],
    "giraffe": [
        "I am very tall",
        "I have a long neck",
        "I eat leaves"
    ]
}

score = 0

print("===== Animal Identification Game =====")

while True:

    animal = random.choice(list(animals.keys()))

    print("\nGuess the Animal!")

    for hint in animals[animal]:
        print("Hint:", hint)

    answer = input("Your Answer: ").lower()

    if answer == animal:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Animal:", animal)

    print("Current Score:", score)

    choice = input("\nPlay Again? (yes/no): ").lower()

    if choice != "yes":
        break

print("\nFinal Score:", score)
print("Thank You For Playing!")
