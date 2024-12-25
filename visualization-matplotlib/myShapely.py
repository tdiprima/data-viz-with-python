# Defines two polygons (one outer and one inner), checks whether the inner polygon is completely within the outer polygon, whether they intersect, and then displays a plot of the polygons.
import sys

import matplotlib.pyplot as plt
from shapely.geometry import Polygon


def check_polygons():
    # Check if the inner polygon is completely within the outer polygon
    if inner_polygon.within(outer_polygon):
        print("The inner polygon is completely inside the outer polygon.")
    else:
        print("The inner polygon is NOT completely inside the outer polygon.")

    # Additionally, you might want to check if the polygons overlap without one being entirely contained within the other
    if outer_polygon.intersects(inner_polygon) and not inner_polygon.within(outer_polygon):
        print("The inner polygon intersects with the outer polygon but is not completely inside it.")


# Function to plot the polygon using matplotlib
def plot_polygon(ax, polygon, color):
    x, y = polygon.exterior.xy
    ax.fill(x, y, alpha=0.5, color=color)


def draw_polygons1():
    # Set up the figure and axis
    fig, ax = plt.subplots()

    # Plot the polygons
    plot_polygon(ax, outer_polygon, 'blue')
    plot_polygon(ax, inner_polygon, 'green')

    # Set the limits of the plot
    minx, miny, maxx, maxy = outer_polygon.bounds
    ax.set_xlim(minx - 1, maxx + 1)
    ax.set_ylim(miny - 1, maxy + 1)
    ax.set_aspect('equal')

    # Show the plot
    plt.show()


def draw_polygons():
    """
    TODO: Note: Descartes is giving me problems.
    PolygonPatch converts Shapely geometries into matplotlib patches
    """
    from descartes import PolygonPatch
    try:
        # Set up the figure and axis
        fig, ax = plt.subplots()

        # Create a patch for the outer polygon
        outer_patch = PolygonPatch(outer_polygon, alpha=0.5, zorder=2)
        ax.add_patch(outer_patch)

        # Create a patch for the inner polygon
        inner_patch = PolygonPatch(inner_polygon, alpha=0.5, zorder=2)
        ax.add_patch(inner_patch)

        # Set the limits of the plot
        minx, miny, maxx, maxy = outer_polygon.bounds
        ax.set_xlim(minx - 1, maxx + 1)
        ax.set_ylim(miny - 1, maxy + 1)
        ax.set_aspect('equal')

        # Show the plot
        plt.show()
    except Exception:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("\nType:", exc_type)
        print("\nErr:", exc_obj)
        print("\nLine:", exc_tb.tb_lineno)
        sys.exit(1)


if __name__ == '__main__':
    # Define the coordinates for the outer polygon
    outer_polygon_coords = [(0, 0), (4, 0), (4, 4), (0, 4)]

    # todo: Define the coordinates for the inner polygon
    inner_polygon_coords = [(1, 1), (3, 1), (3, 3), (1, 3)]  # Inside
    # inner_polygon_coords = [(-1, 1), (1, 1), (1, 3), (-1, 3)]  # Intersects

    # Create the polygon objects
    outer_polygon = Polygon(outer_polygon_coords)
    inner_polygon = Polygon(inner_polygon_coords)

    check_polygons()
    # draw_polygons()
    draw_polygons1()
