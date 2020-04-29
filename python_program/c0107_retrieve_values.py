import math
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

def retrieve_value(variable_name):
    """

    """
    filepath = os.path.join("..", "reference_files")
    filename = os.path.join(filepath, "variables" + ".csv")
    print("finding " +  filename)

    df_named = pd.read_csv(filename)

    variable_name_master = list(df_named['Name'])
    value_master = list(df_named['Value'])

    if variable_name in variable_name_master:
        index = variable_name_master.index(variable_name)
        value = value_master[index]

    else:
        value = 0
        print("Variable not found.")

    return(value)

if __name__ == "__main__":
    variable_name = "area_min"
    print("variable_name " + variable_name)

    value = retrieve_value(variable_name)
    print(variable_name + " = " + str(value))
