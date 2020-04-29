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

def plot_count_per_record():
    """

    """

    print("running plot_count_per_record")

    a = retrieve_value("area_min")
    a_2 = retrieve_value("area_max")
    c = retrieve_value("circularity_min")
    c_2 = retrieve_value("circularity_max")

    record_name_master, count_master = parse_name_and_count()

    fig_rows, fig_columns, subplot_number = 2, 1, 0
    fig = plt.figure(figsize=(fig_columns*20, fig_rows*6))

    subplot_number += 1
    plt.subplot(fig_rows, fig_columns, subplot_number)
    for record_name in record_name_master:

        index = record_name_master.index(record_name)
        area, perim, width, height, circularity = retrieve_by_record_name(record_name)

        area_truncated, circularity_truncated = truncate_two_lists(area, circularity, a, a_2, c, c_2)
        plt.bar([index], [len(area_truncated)], width=0.8, color = [1,0,0])


    plt.title("Summary of Colony Counts")
    plt.xlabel("Record Names")
    plt.ylabel("Counts")
    # plt.ylim([0.1, 1000])
    # plt.yscale('log')

    plt.xlim([-0.5, len(record_name_master)+1])
    xx = np.linspace(0,len(record_name_master)-1, len(record_name_master))
    plt.xticks(xx, record_name_master)

    subplot_number += 1
    plt.subplot(fig_rows, fig_columns, subplot_number)
    for record_name in record_name_master:

        index = record_name_master.index(record_name)
        area, perim, width, height, circularity = retrieve_by_record_name(record_name)

        if index == 0:
            area_truncated, circularity_truncated = truncate_two_lists(area, circularity, 0, a, c, c_2)
            plt.bar([index+.25], [len(area_truncated)], width=0.5, color = [.8,.8,.8], label = "Non-Colonies")

            area_truncated, circularity_truncated = truncate_two_lists(area, circularity, a, a_2, c, c_2)
            plt.bar([index], [len(area_truncated)], width=0.5, color = [1,0,0], label = "Colonies")

        else:
            area_truncated, circularity_truncated = truncate_two_lists(area, circularity, 0, a, c, c_2)
            plt.bar([index+.25], [len(area_truncated)], width=0.5, color = [.8,.8,.8])

            area_truncated, circularity_truncated = truncate_two_lists(area, circularity, a, a_2, c, c_2)
            plt.bar([index], [len(area_truncated)], width=0.5, color = [1,0,0])


        plt.title("Summary of Found Particles (Small vs Large)")
        plt.xlabel("Record Names")
        plt.ylabel("Counts")
        #plt.ylim([0.1, 1000])
        #plt.yscale('log')

        plt.legend(loc='upper right')

        plt.xlim([-0.5, len(record_name_master)+1])
        xx = np.linspace(0,len(record_name_master)-1, len(record_name_master))
        plt.xticks(xx, record_name_master)

    # Name, save, and show the plot
    filepath = os.path.join( "..", "figures", "summary")
    if not os.path.exists(filepath): os.makedirs(filepath)
    filename = os.path.join( filepath, "counts" +'.png')
    plt.savefig(filename, bbox_inches='tight', dpi=300)

    print("saved " + filename)

    print("completed plot_count_per_record")


if __name__ == "__main__":
    plot_count_per_record()
