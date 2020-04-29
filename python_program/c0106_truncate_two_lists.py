import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count
from c0104_retrieve_by_record_name import retrieve_by_record_name

def truncate_two_lists(list_a, list_b, min_a, max_a, min_b, max_b):
    """

    """
    list_a_truncated, list_b_truncated = [], []

    for i in range(len(list_a)):
        if list_a[i] >= min_a:
            if list_a[i] < max_a:
                list_a_truncated.append(list_a[i])
                list_b_truncated.append(list_b[i])

    list_a, list_b = [], []
    for i in range(len(list_b_truncated)):
        if list_b_truncated[i] >= min_b:
            if list_b_truncated[i] < max_b:
                list_a.append(list_a_truncated[i])
                list_b.append(list_b_truncated[i])


    return(list_a, list_b)

if __name__ == "__main__":
    list_a, list_b = truncate_two_lists(list_a, list_b, min_a, max_a, min_b, max_b)
