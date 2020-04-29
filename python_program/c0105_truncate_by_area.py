import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count
from c0104_retrieve_by_record_name import retrieve_by_record_name

def truncate_by_area(area, other, min, max):
    """

    """
    area_truncated, other_truncated = [], []

    for i in range(len(area)):

        if area[i] >= min:
            if area[i] < max:
                area_truncated.append(area[i])
                other_truncated.append(other[i])

    return(area_truncated, other_truncated)

if __name__ == "__main__":
    area_truncated, other_truncated = truncate_by_area(area, other, min, max)
