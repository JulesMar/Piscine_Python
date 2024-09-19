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


def aff_pop(data: pd.DataFrame):
    data.iloc[:, :] = data.iloc[:, :].map(convert_value)
    data = data.drop(columns=data.loc[:, pd.to_numeric(data.columns) > 2050])
    data = data.drop(columns=data.loc[:, pd.to_numeric(data.columns) < 1800])
    france = data.loc["France"].astype(float)
    belgium = data.loc["Belgium"].astype(float)
    france.plot()
    belgium.plot()
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.show()


def main():
    data = load("population_total.csv")
    aff_pop(data)


if __name__ == "__main__":
    main()
