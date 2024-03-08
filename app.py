import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add Page options for overall app.
ui.page_opts(title="JB's PyShiny App with a plot")

with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 50, 25)


@render.plot(alt="A histogram showing random data distro")
def draw_histogram():
    # define the number of points to generate. Use optional type hinting
    count_of_points: int = 437
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    x = 100 + 15 * np.random.randn(437)
    # add different color and edge color to seperate the coloumns~!
    plt.hist(
        random_data_array,
        input.selected_number_of_bins(),
        density=True,
        color="orange",
        edgecolor="green",
        linewidth=1.2,
    )
