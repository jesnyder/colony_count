import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements

def parse_name_and_count():
    """

    """
    df_result, df_summary = retrieve_measurements()

    record_name_master_original = list(df_summary['Slice'])
    count_master = list(df_summary['Count'])

    record_name_master = []
    for item in record_name_master_original:
        if item not in record_name_master:
            record_name_master.append(item)

    count_master = count_master[:len(record_name_master)]

    print(record_name_master)
    print("number of records : " + str(len(record_name_master)))
    print("number of counts : " + str(len(count_master)))

    return(record_name_master, count_master)

if __name__ == "__main__":
    record_name_master, count_master = parse_name_and_count()
