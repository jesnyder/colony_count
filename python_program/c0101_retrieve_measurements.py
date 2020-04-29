import math
import os
import numpy as np
import pandas as pd


def retrieve_measurements():
    """

    """
    print("running retrieve_measurements")

    filepath = os.path.join("..", "original")
    filename = os.path.join(filepath, "all_results.csv")
    df_result = pd.read_csv(filename)

    # del df_result['Unnamed: 0']

    filename = os.path.join(filepath, "all_summary.csv")
    df_summary = pd.read_csv(filename)

    # def df_summary['Unnamed: 0']

    print(df_summary)

    print("completed retrieve_measurements")

    return(df_result, df_summary)


if __name__ == "__main__":
    df_result, df_summary = retrieve_measurements()
