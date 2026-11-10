"""
Author: Maria Herrmann
Created on: 2026-11-09

NOT DONE!

Sample script to translate my Matlab workflow to Python.
(1) Read in two relational tables
(2) Merge the two tables based on a common key
(3) Summarize the values in the merged table based on a grouping variable
(4) Savethe resulting table to a new file
(5) Visualize the results using time series chart, bar chart, scatter plot, box plot, and histogram

In VS Code, # %% is used to create code cells that can be run independently. 
This is useful for testing and debugging specific sections of the code without running the entire script.
"""

# %% 
# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% 
# Constants
TABLE1_PATH = "table1.csv"
TABLE2_PATH = "table2.csv"
MERGED_PATH = "merged.csv"

# %% 
# Functions
def read_table(file_path):
    return pd.read_csv(file_path)

# %% Main script
def main():
    # Read in the two tables
    table1 = read_table(TABLE1_PATH)
    table2 = read_table(TABLE2_PATH)

    # Merge the two tables based on a common key
    merged_table = pd.merge(table1, table2, on="common_key")

    # Summarize the values in the merged table based on a grouping variable
    summary = merged_table.groupby("grouping_variable").agg({"value_column": "sum"})

    # Save the resulting table to a new file
    summary.to_csv(MERGED_PATH)

    # Visualize the results using various plots
    plt.figure(figsize=(10, 6))
    plt.plot(summary.index, summary["value_column"], marker='o')
    plt.title("Time Series Chart")
    plt.xlabel("Grouping Variable")
    plt.ylabel("Summed Values")
    plt.grid()
    plt.show()

# %% 
# Execution
    if __name__ == "__main__":
        main()