from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def aff_life(data: pd.DataFrame):
    data = data.loc["France"]
    data.plot()
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


def main():
    data = load("life_expectancy_years.csv")
    aff_life(data)


if __name__ == "__main__":
    main()
