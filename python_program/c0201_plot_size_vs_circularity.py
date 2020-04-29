import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count
from c0104_retrieve_by_record_name import retrieve_by_record_name
from c0105_truncate_by_area import truncate_by_area
from c0106_truncate_two_lists import truncate_two_lists
from c0107_retrieve_values import retrieve_value

def plot_size_vs_circularity():
    """

    """

    print("running plot_size_vs_circularity")

    a = retrieve_value("area_min")
    a_2 = retrieve_value("area_max")
    c = retrieve_value("circularity_min")
    c_2 = retrieve_value("circularity_max")
    p = math.pow(a*4*math.pi,.5)
    p_2 = math.pow(a_2*4*math.pi,.5)

    # Initiate a new figure
    fig_rows, fig_columns, subplot_number = 5, 5, 0
    fig = plt.figure(figsize=(fig_columns*6, fig_rows*6))

    record_name_master, count_master = parse_name_and_count()

    for record_name in record_name_master:
        area, perim, width, height, circularity = retrieve_by_record_name(record_name)

        fig_rows, fig_columns, subplot_number = 1, 2, 0
        fig = plt.figure(figsize=(fig_columns*6, fig_rows*6))


        subplot_number += 1
        plt.subplot(fig_rows, fig_columns, subplot_number)

        plt.scatter(x = np.linspace(a, a, 100), y = np.linspace(0.9*min(circularity), 1.1*max(circularity), 100), s = 1, color = [.8,0,0], label = str("Min Area = " + str(a)))
        plt.scatter(x = np.linspace(0.9*min(area), 1.1*max(area), 100000), y = np.linspace(c, c, 100000), s = 1, color = [0,0,.8], label = str("Min Circularity = " + str(c)))

        plt.scatter(area, circularity, color = [.8,.8,.8], label = "Non-Colonies")

        area_truncated, circularity_truncated = truncate_two_lists(area, circularity, a, a_2, c, 10)
        plt.scatter(area_truncated, circularity_truncated, color = [1,0,0], label = "Colonies")

        plt.title(record_name)
        plt.xlabel("Area (mm^2)")
        plt.xlim([0.001, 1000])
        plt.xscale('log')
        plt.ylabel("Circularity")
        plt.legend(loc='upper right')


        subplot_number += 1
        plt.subplot(fig_rows, fig_columns, subplot_number)

        area_truncated, circularity_truncated = truncate_two_lists(area, circularity, 0, a, c, 10)
        plt.bar([0], [len(area_truncated)], width=0.8)

        area_truncated, circularity_truncated = truncate_two_lists(area, circularity, 0, a, 0, c)
        plt.bar([2], [len(area_truncated)], width=0.8)

        area_truncated, circularity_truncated = truncate_two_lists(area, circularity, a, a_2, 0, c)
        plt.bar([3], [len(area_truncated)], width=0.8)

        area_truncated, circularity_truncated = truncate_two_lists(area, circularity, a, a_2, c, 10)
        plt.bar([1], [len(area_truncated)], width=0.8)

        plt.title(record_name + " (colony count = " + str(len(area_truncated)) + ")")
        plt.xlabel("Area (mm^2)")
        plt.ylabel("Counts")

        plt.xlim([-0.5, 3.5])
        plt.xticks([0,1,2,3], ["Small \n Circular", "Large \n Circular \n (Colony)", "Small \n Non-Circular", "Large \n Non-Circular"])


        # Name, save, and show the plot
        filepath = os.path.join( "..", "figures", "circularity_vs_area")
        if not os.path.exists(filepath): os.makedirs(filepath)
        filename = os.path.join( filepath, record_name +'.png')
        plt.savefig(filename, bbox_inches='tight', dpi=300)

        print("saved " + filename)

    print("completed plot_size_vs_circularity")


if __name__ == "__main__":
    plot_size_vs_circularity()
