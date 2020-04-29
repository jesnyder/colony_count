import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count

def retrieve_by_record_name(record_name):
    """

    """

    filepath = os.path.join("..", "formatted")
    filename = os.path.join(filepath, record_name + ".csv")

    df_named = pd.read_csv(filename)

    area = list(df_named['Area'])
    perim = list(df_named['Perim'])
    width = list(df_named['Width'])
    height = list(df_named['Height'])
    circularity = list(df_named['Circularity'])


    return(area, perim, width, height, circularity)

if __name__ == "__main__":
    area, perim, width, height, circularity = format_count_by_name(record_name)
