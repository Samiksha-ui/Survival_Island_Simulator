from flask import Flask, jsonify
import sqlite3
import numpy as np

app = Flask(__name__)


def get_database():

    connection = sqlite3.connect("survival.db")

    return connection


@app.route("/survival/<int:day>")
def survival_summary(day):

    connection = get_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT health, water, food, energy, shelter
        FROM survival_data
        WHERE day = ?
    """, (day,))

    rows = cursor.fetchall()

    connection.close()

    if not rows:
        return jsonify({
            "message": "No data found for this day"
        }), 404

    health = [row[0] for row in rows]
    water = [row[1] for row in rows]
    food = [row[2] for row in rows]
    energy = [row[3] for row in rows]

    return jsonify({
        "day": day,
        "average_health": float(np.mean(health)),
        "average_water": float(np.mean(water)),
        "average_food": float(np.mean(food)),
        "average_energy": float(np.mean(energy)),
        "peak_health": int(np.max(health))
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)