import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Example data (theta and radius values)
theta = np.radians([0, 0, 0, 
                    45, 45, 45,
                    90, 90, 90,
                    135, 135, 135,
                    180, 180, 180,
                    225, 225, 225,
                    270, 270, 270,
                    315, 315, 315,
                    360, 360, 360])
radius = [15, 150, 360,
          15, 150, 360,
          15, 150, 360,
          15, 150, 360,
          15, 150, 360,
          15, 150, 360,
          15, 150, 360,
          15, 150, 360,
          15, 150, 360]
#error = [2.07, 3.1, 8.69]
error = [1.57, 1.01, 1.46,
         1.57, 1.01, 1.46,
         1.57, 1.01, 1.46,
         1.57, 1.01, 1.46,
         1.57, 1.01, 1.46,
         1.57, 1.01, 1.46,
         1.57, 1.01, 1.46,
         1.57, 1.01, 1.46,
         1.57, 1.01, 1.46]
'''
theta2 = np.radians([np.rad2deg(np.arctan(115/15)), np.rad2deg(np.arctan(115/150)), np.rad2deg(np.arctan(115/360)), np.rad2deg(np.arctan(115/500)), 90, 25, 90, 31, 90, 28, 90, 27, 90, 27, 90, 90]) #do srediego bledu trzeba dodac 
radius2 = [15, 150, 360, 500, 400, 400, 300, 300, 355, 355, 365, 365, 360, 360, 500, 150] #do sredniego bledu trzeba dodac 
#error2 = [1.99, 1.77, 8.03, 4.85, 19, 3, 19, 3, 19, 3, 19, 3, 19, 3, 19, 19]
error2 = [4.38, 1.62, 11.22, 18.77, 40, 3, 40, 3, 40, 3, 40, 3, 40, 3, 40, 40]

theta3 = np.radians([np.rad2deg(np.arctan(190/15)), np.rad2deg(np.arctan(190/150)), np.rad2deg(np.arctan(190/360)), np.rad2deg(np.arctan(190/500))])
radius3 = [15, 150, 360, 500]
#error3 = [36.12, 8.82, 3.13, 2.54]
error3 = [46.86, 5.71, 4.12, 14.43]

# Combine data from all sets
all_theta = np.concatenate([theta, theta2, theta3, np.pi - theta, np.pi - theta2, np.pi - theta3])
all_radius = np.concatenate([radius, radius2, radius3, radius, radius2, radius3])
all_error = np.concatenate([error, error2, error3, error, error2, error3])
'''
# Set up a grid for interpolation
theta_grid, radius_grid = np.meshgrid(np.linspace(0, 2*np.pi, 1000), np.linspace(0, 500, 1000))

# Interpolate errors onto the grid
error_grid = griddata((theta, radius), error, (theta_grid, radius_grid), method='linear', fill_value=1.57) #20 albo 35


# Create a polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10))

# Plot the interpolated density map as contours
contour = ax.contourf(theta_grid, radius_grid, error_grid, cmap='jet', levels=1000, vmin=1.01, vmax=1.57)   #15 albo 30
'''
# Plot your points on top
ax.scatter(theta, radius, c=error, cmap='jet', s=100, marker='o', edgecolors='w', linewidth=1, vmin=0, vmax=10)
ax.scatter(theta2, radius2, c=error2, cmap='jet', s=100, marker='o', edgecolors='w', linewidth=1, vmin=0, vmax=10)
ax.scatter(theta3, radius3, c=error3, cmap='jet', s=100, marker='o', edgecolors='w', linewidth=1, vmin=0, vmax=10)
'''

# Set radial axis limits for better visibility
ax.set_rmax(360)  # Adjust as needed

# Set colorbar
cbar = plt.colorbar(contour, ax=ax, label='Odchylenie standardowe [$^{\circ}$]')

# You can customize the polar plot if needed
plt.title("Charakterystyka kąta elewacji węzła akustycznego wyznaczona na podstawie interpolacji odchylenia standardowego na wysokości 0.10 m")
plt.grid(True)

# Show the plot
plt.show()
