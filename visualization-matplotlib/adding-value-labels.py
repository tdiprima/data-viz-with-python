# This code generates a bar chart that visualizes College Admissions by Courses.
# The x-axis represents various Courses (such as "Engineering", "Hotel Management", etc) 
# and the y-axis represents the number of admissions in each course.
# The add_labels function places value labels on each bar in the chart.
# The figure size, title and axis labels are also set in this script.
# Finally, the "plt.show()" command displays the created bar chart on screen.
# https://www.geeksforgeeks.org/adding-value-labels-on-a-matplotlib-bar-chart/
import matplotlib.pyplot as plt


# function to add value labels
def add_labels(x1, y1):
    for i in range(len(x1)):
        plt.text(i, y1[i], y1[i], ha='center')


if __name__ == '__main__':
    # creating data on which bar chart will be plotted
    x = ["Engineering", "Hotel Management",
         "MBA", "Mass Communication", "BBA",
         "BSc", "MSc"]
    y = [9330, 4050, 3030, 5500,
         8040, 4560, 6650]

    # setting figure size by using figure() function
    plt.figure(figsize=(10, 5))

    # making the bar chart on the data
    plt.bar(x, y)

    # calling the function to add value labels
    add_labels(x, y)

    # giving title to the plot
    plt.title("College Admission", fontsize=14)

    # giving X and Y labels
    plt.xlabel("Courses", fontsize=14)
    plt.ylabel("Number of Admissions", fontsize=14)

    # ax = plt.gca()
    # ax.set_ylim([0, 0.6])
    # plt.grid(True)

    # visualizing the plot
    plt.show()

exit(0)
