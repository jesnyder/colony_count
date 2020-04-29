import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count
from c0104_retrieve_by_record_name import retrieve_by_record_name

from c0201_plot_size_vs_circularity import plot_size_vs_circularity
from c0202_plot_count_per_record import plot_count_per_record

def plot_colony_count():
    """

    """
    print("running plot_colony_count")

    plot_count_per_record()

    plot_size_vs_circularity()

    print("completed plot_colony_count")

if __name__ == "__main__":
    plot_colony_count()
