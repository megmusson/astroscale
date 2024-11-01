import numpy as np
import matplotlib.pyplot as plt
import csv
from functions import read_data_from_csv
from functions import read_rotation_data
import math


gt_euler = read_rotation_data('data/rotation/Viscam-W/10d_rotating_horizontal/gt_euls.csv')

est_euler = read_data_from_csv('data/rotation/Viscam-W/10d_rotating_horizontal/Mk6_Eul_res.csv')




angle =  np.array([item[1] for item in gt_euler])
gt_yaw = np.array([item[4] for item in gt_euler])
gt_pitch = np.array([item[3] for item in gt_euler])
gt_roll = np.array([item[2] for item in gt_euler])
data_yaw = np.array([item[3] for item in est_euler]) # X error from eul_error (2nd column)
data_pitch = np.array([item[2] for item in est_euler])
data_roll = np.array([item[1] for item in est_euler])


gt_yaw[gt_yaw < 0] = 2*np.pi + gt_yaw[gt_yaw < 0]
data_yaw[data_yaw < 0] = 2*np.pi + data_yaw[data_yaw < 0]

# gt_roll[gt_roll < 0] = 2*np.pi + gt_roll[gt_roll < 0]
# data_roll[data_roll < 0] = 2*np.pi + data_roll[data_roll < 0]

gt_yaw = gt_yaw * 180 / np.pi
gt_pitch = gt_pitch * 180 / np.pi
gt_roll = gt_roll * 180 / np.pi
data_yaw = data_yaw * 180 / np.pi
data_pitch = data_pitch * 180 / np.pi
data_roll = data_roll * 180 / np.pi

################# X ERROR ##################
# Create a scatter plot 
plt.figure(1, figsize=(10, 4))
plt.grid(True, zorder=1)
plt.scatter(angle, gt_yaw, c='red', label='Ground Truth', alpha=0.6)
plt.scatter(angle[1:-1], data_yaw, c='blue', label='X estimate', alpha=0.6)
plt.scatter(-80, 180, color='blue', marker='x', linewidths=1)
plt.scatter(80, 180, color='blue', marker='x', linewidths=1)
plt.xlabel('Pitch (Y) Rotation [°]')
plt.ylabel('Euler Angle Yaw (X) [°]')
plt.title('Euler Angle X ground truth and estimate comparison')
plt.xlim(-85, 85)
plt.grid(True)
plt.legend()


################# Y ERROR ##################
# Create a scatter plot 
plt.figure(2, figsize=(10, 4))
plt.grid(True, zorder=1)
plt.scatter(angle, gt_pitch, c='red', label='Ground Truth', alpha=0.6)
plt.scatter(angle[1:-1], data_pitch, c='blue', label='Y estimate', alpha=0.6)
plt.scatter(-80, -80, color='blue', marker='x', linewidths=1)
plt.scatter(80, 80, color='blue', marker='x', linewidths=1)
plt.xlabel('Pitch (Y) Rotation [°]')
plt.ylabel('Euler Angle Pitch (Y) [°]')
plt.title('Euler Angle Y ground truth and estimate comparison')
plt.xlim(-85, 85)
plt.grid(True)
plt.legend()

################# Z ERROR ##################
# Create a scatter plot 
plt.figure(3, figsize=(10, 4))
plt.grid(True, zorder=1)
plt.scatter(angle, gt_roll, c='red', label='Ground Truth', alpha=0.6)
plt.scatter(angle[1:-1], -data_roll, c='blue', label='Z estimate', alpha=0.6)
plt.scatter(-80, 0, color='blue', marker='x', linewidths=1)
plt.scatter(80, 0, color='blue', marker='x', linewidths=1)
plt.xlabel('Pitch (Y) Rotation [°]')
plt.ylabel('Euler Angle Roll (Z) [°]')
plt.title('Euler Angle Z ground truth and estimate comparison')
plt.xlim(-85, 85)
plt.grid(True)
plt.legend()


plt.show()


# gt_euler = read_data_from_csv('data/distance/W/10d_random_xy_const_z/gt_euls.csv')

# est_euler = read_data_from_csv('data/distance/W/10d_random_xy_const_z/Mk6_Eul_res.csv')

# num =  np.array([item[0] for item in gt_euler])
# yaw = np.array([item[1] for item in gt_euler])
# pitch = np.array([item[2] for item in gt_euler])
# roll = np.array([item[3] for item in gt_euler])
# data_pitchaw = np.abs(np.array([item[1] for item in est_euler]))  # X error from eul_error (2nd column)
# data_pitch = np.abs(np.array([item[2] for item in est_euler]))
# data_roll = np.abs(np.array([item[3] for item in est_euler]))


# ################# X ERROR ##################
# # Create a scatter plot 
# plt.figure(1, figsize=(8.18, 6.1))
# plt.grid(True, zorder=1)
# # plt.plot(num, yaw, marker='o', label='Xgt', color='C0')
# # plt.plot(num, data_pitchaw, marker='x', label='Xestimate', color='forestgreen')

# plt.scatter(num, yaw, c='red', label='Ground Truth', alpha=0.6)
# plt.scatter(num, data_pitchaw, c='blue', label='X estimate', alpha=0.6)
# plt.scatter(num, data_pitch, c='green', label='Y estimate', alpha=0.6)
# plt.xlabel('Image #')
# plt.ylabel('Euler Angle')
# plt.title('Euler Angle X Y ground truth and estimate comparison')
# plt.xlim(0, 101)
# plt.grid(True)
# plt.legend()


# ################# Z ERROR ##################
# # Create a scatter plot 
# plt.figure(3, figsize=(8.18, 6.1))
# plt.grid(True, zorder=1)
# plt.scatter(num, roll, c='red', label='Ground Truth', alpha=0.6)
# plt.scatter(num, -data_roll, c='blue', label='Z estimate', alpha=0.6)
# plt.xlabel('Image #')
# plt.ylabel('Euler Angle Z')
# plt.title('Euler Angle Z ground truth and estimate comparison')
# plt.xlim(0, 101)
# plt.grid(True)
# plt.legend()


# plt.show()

