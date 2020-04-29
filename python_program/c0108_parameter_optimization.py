import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count
from c0103_format_count_by_name import format_count_by_name
from c0104_retrieve_by_record_name import retrieve_by_record_name

def parameter_optimiation():
    """

    """
    record_name_master, count_master = parse_name_and_count()

    record_name_neg = record_name_master[0]
    record_name_pos1 = record_name_master[1]
    record_name_pos2 = record_name_master[2]

    area, perim, width, height, circularity = retrieve_by_record_name(record_name_neg)

    area_neg_max = min(area)
    for i in range(len(area)):
        if circularity[i] > 0.6:
            if area[i] < 15:
                if area[i] > area_neg_max:
                    area_neg_max = area[i]

    area, perim, width, height, circularity = retrieve_by_record_name(record_name_pos1)

    circularity_min = max(circularity)
    for i in range(len(circularity)):
        if circularity[i] > 0.5:
            if area[i] >= area_neg_max:
                if circularity_min > circularity[i]:
                    circularity_min = circularity[i]

    print("Max Neg Area: " + str(area_neg_max))
    print("Max Neg Circularity: " + str(circularity_min))

    df_named = pd.DataFrame()
    df_named["Max Neg Area"] = [area_neg_max]
    df_named["Max Neg Circularity"] = [circularity_min]

    filepath = os.path.join("..", "reference_files")
    if not os.path.exists(filepath): os.makedirs(filepath)
    filename = os.path.join(filepath, "parameter_optimiation" + ".csv")
    # df_named.to_csv(filename, sep=(','))

if __name__ == "__main__":
    parameter_optimiation()
