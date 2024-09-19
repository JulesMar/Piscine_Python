from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def convert_value(value):
    if isinstance(value, str):
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
        elif 'B' in value:
            return float(value.replace('B', '')) * 1e9
    return float(value)


def projection_life(income: pd.DataFrame, life: pd.DataFrame):
    life = life.loc[:, "1900"]
    income = income.loc[:, "1900"]
    plt.scatter(income, life)
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.xlim(left=300)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()


def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    projection_life(income, life)


if __name__ == "__main__":
    main()
