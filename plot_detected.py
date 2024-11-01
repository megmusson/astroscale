import numpy as np
import matplotlib.pyplot as plt
import csv
from functions import distance_to_fov


def plot_detection_results(gt, tvec, distance):

    # Assuming gt_tvec_res is a list of lists (or a similar structure)
    gt = np.array(gt)  
    tvec = np.array(tvec)  

    # Create a set of detected image numbers for easy lookup
    detected_images = set(int(x[0]) for x in tvec)

    # Separate ground truth into detected and undetected - mask is array of true or false
    detected_mask = np.array([int(i[0]) in detected_images for i in gt[1:]])
    not_detected_mask = ~detected_mask

    # gt_detected = gt[detected_mask]
    gt_detected = np.array(gt[1:])[detected_mask]
    # not_detected = gt[not_detected_mask]s
    not_detected = np.array(gt[1:])[not_detected_mask]

    # Create the plot
    plt.figure(figsize=(8.18, 6.1))
    plt.scatter(gt_detected[:, 1], gt_detected[:, 2], c='green', label='Detected', alpha=0.6)
    plt.scatter(not_detected[:, 1], not_detected[:, 2], c='red', label='Not Detected', alpha=0.6)

    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    x_range, y_range = distance_to_fov(distance)
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)

    plt.gca().invert_yaxis()

    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.title('Marker Detection Results with XY Position at 3m, constant dark lighting')
    plt.legend()

    # Set equal aspect ratio and center at 0,0
    plt.axis('equal')
    plt.grid(True, alpha=0.3)

    plt.show()