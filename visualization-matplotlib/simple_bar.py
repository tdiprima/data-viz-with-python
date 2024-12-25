# This script generates a bar chart representing the GDP Per Capita of several countries, 
# using the matplotlib library in Python. The countries included are USA, Canada, Germany, UK, and France. 
# Each country bar on the graph is given a distinct color. The x-axis represents the country names and 
# the y-axis represents the GDP Per Capita. The title of the graph is 'Country Vs GDP Per Capita'.
# The graph also includes a grid for better visualization of data points.
import matplotlib.pyplot as plt

Country = ['USA', 'Canada', 'Germany', 'UK', 'France']
GDP_Per_Capita = [45000, 42000, 52000, 49000, 47000]

New_Colors = ['green', 'blue', 'purple', 'brown', 'teal']
plt.bar(Country, GDP_Per_Capita, color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()
# https://datatofish.com/bar-chart-python-matplotlib/
import matplotlib.pyplot as plt

Country = ['USA', 'Canada', 'Germany', 'UK', 'France']
GDP_Per_Capita = [45000, 42000, 52000, 49000, 47000]

New_Colors = ['green', 'blue', 'purple', 'brown', 'teal']
plt.bar(Country, GDP_Per_Capita, color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()
