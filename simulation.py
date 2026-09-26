import random


def get_weather():
    weather = random.choice([
        "Sunny",
        "Rainy",
        "Stormy",
        "Cloudy"
    ])

    return weather


def perform_action(action, health, water, food, energy, shelter):

    message = ""

    if action == "Collect Water":

        water += 30
        energy -= 10
        message = "You collected fresh water."

    elif action == "Hunt":

        food += 30
        energy -= 20
        message = "You found food while hunting."

    elif action == "Gather Wood":

        shelter += 20
        energy -= 15
        message = "You gathered wood and improved your shelter."

    elif action == "Rest":

        energy += 30
        health += 5
        message = "You rested and recovered."

    elif action == "Explore":

        energy -= 25

        event = random.choice([
            "You found berries!",
            "You discovered a water source!",
            "A wild animal attacked you!",
            "You found useful materials!"
        ])

        message = event

        if event == "You found berries!":
            food += 20

        elif event == "You discovered a water source!":
            water += 20

        elif event == "A wild animal attacked you!":
            health -= 20

        elif event == "You found useful materials!":
            shelter += 10

    # Keep values between 0 and 100

    health = max(0, min(100, health))
    water = max(0, min(100, water))
    food = max(0, min(100, food))
    energy = max(0, min(100, energy))
    shelter = max(0, min(100, shelter))

    return health, water, food, energy, shelter, message


def end_day(water, food, energy):

    water -= 10
    food -= 10
    energy -= 5

    water = max(0, water)
    food = max(0, food)
    energy = max(0, energy)

    return water, food, energy