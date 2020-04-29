import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count

def format_count_by_name():
    """

    """
    df_result, df_summary = retrieve_measurements()

    record_name_master, count_master = parse_name_and_count()

    print(df_result)

    position = 0
    for record_name in record_name_master:
        print("record_name : " + str(record_name))
        count = count_master[record_name_master.index(record_name)]
        print("count : " + str(count))
        position_2 = position+count
        print("position 1 : 2 | " + str(position) + " :  " + str(position_2))

        df_named = pd.DataFrame()

        column_names = ["Area", "Perim", "Width", "Height"]
        for column_name in column_names:
            area = list(df_result['Area'])
            area = area[position:position_2]
            df_named['Number'] = np.linspace(1,len(area), len(area))
            df_named['Area'] = area

            perim = list(df_result['Perim.'])
            perim = perim[position:position_2]
            df_named['Perim'] = perim

            width = list(df_result['Width'])
            width = width[position:position_2]
            df_named['Width'] = width

            height = list(df_result['Height'])
            height = height[position:position_2]
            df_named['Height'] = height

        circularity = []
        for i in range(len(perim)):
            c = 4*math.pi*area[i]/(math.pow(perim[i],2))
            circularity.append(c)


        df_named['Circularity'] = circularity

        print("length of colonies: " + str(len(area)) + " / " + str(count))

        assert len(area) == count

        filepath = os.path.join("..", "formatted")
        if not os.path.exists(filepath): os.makedirs(filepath)
        filename = os.path.join(filepath, record_name + ".csv")

        df_named.to_csv(filename, sep=(','))

        position += count

if __name__ == "__main__":
    format_count_by_name()
