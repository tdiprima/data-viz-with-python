# This Python script is used for data analysis on sales data stored in a CSV file.
# It uses the pandas library to read the data from the referenced CSV file into a DataFrame, where specific columns (SalesID and ProductPrice) are extracted and converted into numpy arrays.
# These data arrays are then visualized in a line graph using matplotlib, with the SalesID and ProductPrice as the x and y-axes, respectively.
# The 'ggplot' style is used for the plot, and the resultant graph is displayed with a title "Sales Analysis".
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
