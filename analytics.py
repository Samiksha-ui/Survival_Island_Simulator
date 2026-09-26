import pandas as pd
import numpy as np


def create_survival_dataframe(survival_data):

    df = pd.DataFrame(survival_data)

    # Remove empty values
    df = df.dropna()

    # Remove duplicate records
    df = df.drop_duplicates()

    return df


def calculate_statistics(df):

    statistics = {
        "average_health": np.mean(df["Health"]),
        "average_water": np.mean(df["Water"]),
        "average_food": np.mean(df["Food"]),
        "average_energy": np.mean(df["Energy"]),
        "peak_health": np.max(df["Health"]),
        "lowest_health": np.min(df["Health"]),
        "average_shelter": np.mean(df["Shelter"])
    }

    return statistics