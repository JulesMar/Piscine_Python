import pandas as pd


def load(path: str) -> pd.DataFrame:
    if path is None:
        print("No path given")
        return None
    if not path.endswith("csv"):
        print("Wrong extension file please give .csv file")
        return None
    try:
        data = pd.read_csv(path, index_col=0)
    except Exception:
        print(f"Error while reading file {path}")
        return None
    print(f"Loading dataset of dimensions {data.shape}")
    return data
