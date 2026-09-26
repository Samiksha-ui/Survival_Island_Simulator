import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from simulation import (
    get_weather,
    perform_action,
    end_day
)
from analytics import (
    create_survival_dataframe,
    calculate_statistics
)
from database import (
    create_database,
    save_survival_data
)

st.set_page_config(
    page_title="Survival Island Simulator",
    page_icon="🌴"
)
# Load CSS
css_file = Path("static/style.css")

if css_file.exists():
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
        # Create database
create_database()


# -----------------------------
# INITIAL GAME VALUES
# -----------------------------

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "day" not in st.session_state:
    st.session_state.day = 1

if "health" not in st.session_state:
    st.session_state.health = 100

if "water" not in st.session_state:
    st.session_state.water = 100

if "food" not in st.session_state:
    st.session_state.food = 100

if "energy" not in st.session_state:
    st.session_state.energy = 100

if "shelter" not in st.session_state:
    st.session_state.shelter = 20

if "survival_history" not in st.session_state:
    st.session_state.survival_history = []


# -----------------------------
# PLAYER SETUP
# -----------------------------

if not st.session_state.game_started:

    st.title("🌴 Survival Island Simulator")

    st.write(
        "You are stranded on a mysterious island. "
        "Your goal is to survive for as many days as possible."
    )

    st.subheader("👤 Player Setup")

    player_name = st.text_input("Enter your name")

    difficulty = st.selectbox(
        "Choose Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("🏝️ Start Survival"):

        if player_name == "":
            st.warning("Please enter your name.")

        else:
            st.session_state.game_started = True
            st.session_state.player_name = player_name
            st.session_state.difficulty = difficulty

            st.rerun()


# -----------------------------
# SURVIVAL DASHBOARD
# -----------------------------

else:

    st.title("🌴 Survival Island")

    st.write(
        f"Welcome, **{st.session_state.player_name}**!"
    )

    st.subheader(
        f"📅 Day {st.session_state.day}"
    )

    # -----------------------------
    # WEATHER
    # -----------------------------

    weather = get_weather()

    st.write(f"🌦️ Weather: **{weather}**")


    # -----------------------------
    # RESOURCE DISPLAY
    # -----------------------------

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "❤️ Health",
            st.session_state.health
        )

    with col2:
        st.metric(
            "💧 Water",
            st.session_state.water
        )

    with col3:
        st.metric(
            "🍖 Food",
            st.session_state.food
        )

    with col4:
        st.metric(
            "⚡ Energy",
            st.session_state.energy
        )

    with col5:
        st.metric(
            "🏠 Shelter",
            st.session_state.shelter
        )


    st.divider()

    st.subheader("🧭 Choose Your Action")


    # -----------------------------
    # FIRST ROW OF ACTIONS
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("💧 Collect Water"):

            (
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter,
                message
            ) = perform_action(
                "Collect Water",
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter
            )

            st.success(message)


    with col2:

        if st.button("🍖 Hunt"):

            (
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter,
                message
            ) = perform_action(
                "Hunt",
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter
            )

            st.success(message)


    with col3:

        if st.button("🪵 Gather Wood"):

            (
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter,
                message
            ) = perform_action(
                "Gather Wood",
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter
            )

            st.success(message)


    # -----------------------------
    # SECOND ROW OF ACTIONS
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("😴 Rest"):

            (
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter,
                message
            ) = perform_action(
                "Rest",
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter
            )

            st.success(message)


    with col2:

        if st.button("🗺️ Explore"):

            (
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter,
                message
            ) = perform_action(
                "Explore",
                st.session_state.health,
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy,
                st.session_state.shelter
            )

            st.info(message)


    with col3:

        if st.button("🌙 End Day"):

            # Save today's survival data
            st.session_state.survival_history.append({
                "Day": st.session_state.day,
                "Action": "End Day",
                "Health": st.session_state.health,
                "Water": st.session_state.water,
                "Food": st.session_state.food,
                "Energy": st.session_state.energy,
                "Shelter": st.session_state.shelter
            })
            save_survival_data(
    st.session_state.day,
    st.session_state.health,
    st.session_state.water,
    st.session_state.food,
    st.session_state.energy,
    st.session_state.shelter
)

            # Consume daily resources
            (
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy
            ) = end_day(
                st.session_state.water,
                st.session_state.food,
                st.session_state.energy
            )

            st.session_state.day += 1

            st.rerun()


    # -----------------------------
    # SURVIVAL ALERTS
    # -----------------------------

    st.divider()

    st.subheader("⚠️ Survival Alerts")

    if st.session_state.water < 30:
        st.warning(
            "💧 Your water level is dangerously low!"
        )

    if st.session_state.food < 30:
        st.warning(
            "🍖 Your food supply is running low!"
        )

    if st.session_state.energy < 30:
        st.warning(
            "⚡ Your energy is very low. Consider resting!"
        )

    if st.session_state.health < 30:
        st.error(
            "❤️ Your health is critically low!"
        )

    if (
        st.session_state.water >= 30
        and st.session_state.food >= 30
        and st.session_state.energy >= 30
        and st.session_state.health >= 30
    ):
        st.success(
            "✅ Your survival condition is stable."
        )


    # -----------------------------
    # SURVIVAL HISTORY
    # -----------------------------

    st.divider()

    st.subheader("📊 Survival History")

    if len(st.session_state.survival_history) > 0:

        history_df = pd.DataFrame(
            st.session_state.survival_history
        )

        st.dataframe(history_df)

    else:

        st.info(
            "No survival history recorded yet."
        )
        # -----------------------------
# SURVIVAL ANALYTICS
# -----------------------------

st.divider()

st.subheader("📈 Survival Analytics")

if len(st.session_state.survival_history) > 0:

    # Create DataFrame
    analytics_df = create_survival_dataframe(
        st.session_state.survival_history
    )

    # Calculate statistics
    statistics = calculate_statistics(
        analytics_df
    )

    st.write("### 📊 Survival Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Health",
            round(statistics["average_health"], 2)
        )

    with col2:
        st.metric(
            "Average Water",
            round(statistics["average_water"], 2)
        )

    with col3:
        st.metric(
            "Average Food",
            round(statistics["average_food"], 2)
        )

    with col4:
        st.metric(
            "Average Energy",
            round(statistics["average_energy"], 2)
        )

    # -----------------------------
    # HEALTH GRAPH
    # -----------------------------

    st.write("### ❤️ Health Over Time")

    fig, ax = plt.subplots()

    ax.plot(
        analytics_df["Day"],
        analytics_df["Health"],
        marker="o"
    )

    ax.set_xlabel("Day")
    ax.set_ylabel("Health")
    ax.set_title("Health vs Survival Days")

    st.pyplot(fig)

    # -----------------------------
    # RESOURCE GRAPH
    # -----------------------------

    st.write("### 📊 Resource Levels")

    fig, ax = plt.subplots()

    ax.plot(
        analytics_df["Day"],
        analytics_df["Water"],
        marker="o",
        label="Water"
    )

    ax.plot(
        analytics_df["Day"],
        analytics_df["Food"],
        marker="o",
        label="Food"
    )

    ax.plot(
        analytics_df["Day"],
        analytics_df["Energy"],
        marker="o",
        label="Energy"
    )

    ax.set_xlabel("Day")
    ax.set_ylabel("Resource Level")
    ax.set_title("Resources Over Survival Days")

    ax.legend()

    st.pyplot(fig)

else:

    st.info(
        "Play the game and end at least one day "
        "to generate survival analytics."
    )