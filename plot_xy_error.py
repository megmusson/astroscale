import numpy as np
import matplotlib.pyplot as plt
import csv
from functions import distance_to_fov




def plot_error(gt, data, distance):

    ############# EXTRACT DATA ##################
    gt_x = np.array([item[1] for item in gt])
    gt_y = np.array([item[2] for item in gt])
    gt_z = np.array([item[3] for item in gt])
    data_x = np.abs(np.array([item[1] for item in data]))  # X error from eul_error (2nd column)
    data_y = np.abs(np.array([item[2] for item in data]))
    data_z = np.abs(np.array([item[3] for item in data]))


    ################# X ERROR ##################
    # Create a scatter plot 
    plt.figure(1, figsize=(8.18, 6.1))
    plt.grid(True, zorder=1)
    scatter = plt.scatter(gt_x, gt_y, c=data_x, cmap='YlOrBr', edgecolor='gray', linewidth=0.1, s=70)
    cbar = plt.colorbar(scatter)
    cbar.set_label('X Error')
    # Add grid lines and center the axes at (0,0)
    plt.axhline(0, color='black',linewidth=1.5)
    plt.axvline(0, color='black',linewidth=1.5)
    x_range, y_range = distance_to_fov(distance)
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)
    # Add axis labels and a title
    plt.xlabel('X Distance [m]')
    plt.ylabel('Y Distance [m]')
    plt.title('Absolute X Error at various marker locations')
    # Show the plot

    # Y ERROR
    # Create a scatter plot
    y_error = plt.figure(2, figsize=(8.18, 6.1))
    plt.grid(True, zorder=1)
    y_error_scatter = plt.scatter(gt_x, gt_y, c=data_y, cmap='YlOrBr', edgecolor='gray', linewidth=0.1, s=70)
    cbar = plt.colorbar(y_error_scatter)
    cbar.set_label('Y Error')
    x_range, y_range = distance_to_fov(distance)
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)
    # Add grid lines and center the axes at (0,0)
    plt.axhline(0, color='black',linewidth=1.5)
    plt.axvline(0, color='black',linewidth=1.5)
    # Add axis labels and a title
    plt.xlabel('X Distance [m]')
    plt.ylabel('Y Distance [m]')
    plt.title('Absolute Y Error at various marker locations')


    # Z ERROR
    # Create a scatter plot
    z_error = plt.figure(3, figsize=(8.18, 6.1))
    plt.grid(True, zorder=1)
    y_error_scatter = plt.scatter(gt_x, gt_y, c=data_z, cmap='YlOrBr', edgecolor='gray', linewidth=0.1, s=70)
    cbar = plt.colorbar(y_error_scatter)
    cbar.set_label('Z Error')
    x_range, y_range = distance_to_fov(distance)
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)
    # Add grid lines and center the axes at (0,0)
    plt.axhline(0, color='black',linewidth=1.5)
    plt.axvline(0, color='black',linewidth=1.5)
    # Add axis labels and a title
    plt.xlabel('X Distance [m]')
    plt.ylabel('Y Distance [m]')
    plt.title('Absolute Z Error at various marker locations')

    plt.show()


