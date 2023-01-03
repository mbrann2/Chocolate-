import numpy as np
import pandas as pd


def read_file(csv_file):

    df = pd.read_csv(csv_file)
    return df


if __name__ == "__main__":

    chocolate_data = read_file("data/Chocolate_bar_ratings_2022.csv")
    print(chocolate_data)
