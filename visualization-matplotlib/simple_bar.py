# Generates a bar chart representing GDP per Capita of particular countries using matplotlib library in python.
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
