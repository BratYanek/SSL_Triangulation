import matplotlib.pyplot as plt

                                                                ##############################
                                                                #                            #
                                                                #       DRAWING GRAPH        #
                                                                #                            #
                                                                ##############################

def plot_point(ax, x, y, z, color, label):
    ax.scatter(x, y, z, color=color, label=label)

def plot_line(ax, x, y, z, direction_vector, line_length, color, label):
    ax.plot([x, x + line_length * direction_vector[0]],
            [y, y + line_length * direction_vector[1]],
            [z, z + line_length * direction_vector[2]],
            color=color, label=label)
    
def create_3d_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    return ax

def set_axes_labels(ax):
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

def set_aspect_ratio(ax):
    ax.set_box_aspect([1, 1, 1])

def show_plot(ax):
    ax.legend()
    plt.show()