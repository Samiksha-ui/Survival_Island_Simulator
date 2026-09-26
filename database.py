import sqlite3


def create_database():

    connection = sqlite3.connect("survival.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS survival_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day INTEGER,
            health INTEGER,
            water INTEGER,
            food INTEGER,
            energy INTEGER,
            shelter INTEGER
        )
    """)

    connection.commit()
    connection.close()


def save_survival_data(
    day,
    health,
    water,
    food,
    energy,
    shelter
):

    connection = sqlite3.connect("survival.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO survival_data
        (day, health, water, food, energy, shelter)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        day,
        health,
        water,
        food,
        energy,
        shelter
    ))

    connection.commit()
    connection.close()