# Reads Sales data from a CSV file, extracts the 'SalesID' and 'ProductPrice' columns, and visualizes it using a plot, with 'SalesID' on the X-axis and 'ProductPrice' on the Y-axis.
# https://github.com/geekcomputers/Python/blob/master/ReadFromCSV.py

import pandas as pd  # pandas library to read csv file
from matplotlib import pyplot as plt  # matplotlib library to visualise the data
from matplotlib import style

style.use("ggplot")

"""reading data from SalesData.csv file
    and passing data to dataframe"""

# df = pd.read_csv("./SalesData.csv")  # Reading the csv file
df = pd.read_csv("./salesdata1.csv")  # Reading the csv file

"""
pd.DataFrame.as_matrix has been deprecated since version 0.23.0;
you should use DataFrame.to_numpy() instead
"""
# x = df["SalesID"].as_matrix()  # casting SalesID to list #extracting the column with name SalesID
# y = df["ProductPrice"].as_matrix()  # casting ProductPrice to list
x = df["SalesID"].to_numpy()
y = df["ProductPrice"].to_numpy()

plt.xlabel("SalesID")  # assigning X-axis label
plt.ylabel("ProductPrice")  # assigning Y-axis label

plt.title("Sales Analysis")  # assigning Title to the graph
plt.plot(x, y)  # Plot X and Y axis
plt.show()  # Show the graph
