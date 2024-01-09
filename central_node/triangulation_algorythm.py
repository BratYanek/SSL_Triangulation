import numpy as np
import graph
import triangulation_calculations as calc

                                                                #########################################
                                                                #                                       #
                                                                #       TRIANGULATION ALGORYTHM         #
                                                                #                                       #
                                                                #########################################

def triangulation(data_matrix):
    # Given points
    node_matrix = np.array([[1,  1, 0.5],
                            [0,  1, 0.5]])

    # Angles in degrees
    
    azimuth1 = data_matrix[0][1]
    elevation1 = data_matrix[0][2]
    azimuth2 = data_matrix[1][1]
    elevation2 = data_matrix[1][2]


    print(azimuth1, elevation1, azimuth2, elevation2)

    # Convert angles to radians
    azimuth_rad1, elevation_rad1 = calc.convert_to_radians(azimuth1), calc.convert_to_radians(elevation1)
    azimuth_rad2, elevation_rad2 = calc.convert_to_radians(azimuth2), calc.convert_to_radians(elevation2)

    # Calculate direction vectors
    direction_vector1 = calc.calculate_direction_vector(azimuth_rad1, elevation_rad1)
    direction_vector2 = calc.calculate_direction_vector(azimuth_rad2, elevation_rad2)

   

    # Find intersection point
    intersection_point = calc.find_intersection_point(np.array([node_matrix[0][0], node_matrix[0][1], node_matrix[0][2]]), direction_vector1,
                                                      np.array([node_matrix[1][0], node_matrix[1][1], node_matrix[1][2]]), direction_vector2)

    if intersection_point is not None:
        print(f"Intersection point: {intersection_point}")
        with open('data.txt', 'a') as file:
            file.write(' '.join(map(str, intersection_point)) + '\n')

    else:
        # Find nearest distance
        nearest_distance, nearest_point_line1, nearest_point_line2 = calc.find_nearest_distance(
            np.array([node_matrix[0][0], node_matrix[0][1], node_matrix[0][2]]), direction_vector1,
            np.array([node_matrix[1][0], node_matrix[1][1], node_matrix[1][2]]), direction_vector2
        )
        #print(f"Nearest distance between directions: {nearest_distance}")

        # Find and plot midpoint
        midpoint = calc.find_midpoint(nearest_point_line1, nearest_point_line2)

        # Print midpoint
        print(f"Midpoint coordinates: {midpoint}")
        with open('data.txt', 'a') as file:
            file.write(' '.join(map(str, midpoint)) + '\n')

                                                                #######################################
                                                                #       DRAWING GRAPH SECTION         #
                                                                #     commented on the main work      #
                                                                #       for better performance        #
                                                                #######################################
'''
    ax = graph.create_3d_plot()
    graph.plot_point(ax, midpoint[0], midpoint[1], midpoint[2], 'orange', 'Midpoint')

    # Plot points
    graph.plot_point(ax, node_matrix[0][0], node_matrix[0][1], node_matrix[0][2], 'red', 'node_1')
    graph.plot_point(ax, node_matrix[1][0], node_matrix[1][1], node_matrix[1][2], 'red', 'node_2')

    # Plot lines
    line_length = 10
    graph.plot_line(ax, node_matrix[0][0], node_matrix[0][1], node_matrix[0][2], direction_vector1, line_length, 'blue', 'DoA_node_1')
    graph.plot_line(ax, node_matrix[1][0], node_matrix[1][1], node_matrix[1][2], direction_vector2, line_length, 'green', 'DoA_node_2')


    if intersection_point is not None:
        # Plot intersection point
        graph.plot_point(ax, intersection_point[0], intersection_point[1], intersection_point[2], 'black', 'Intersection Point')

    # Plot nearest distance
    ax.plot([nearest_point_line1[0], nearest_point_line2[0]],
            [nearest_point_line1[1], nearest_point_line2[1]],
            [nearest_point_line1[2], nearest_point_line2[2]],
            linestyle='dashed', color='purple', label='Nearest Distance')



    # Set labels and aspect ratio
    graph.set_axes_labels(ax)
    graph.set_aspect_ratio(ax)

    # Show the plot
    graph.show_plot(ax)

data_matrix = np.array([[0, 225, 20],
                        [0, 135, 25]])
triangulation(data_matrix)
'''