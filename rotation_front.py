import numpy as np
import matplotlib.pyplot as plt
from functions import read_data_from_csv
from functions import read_rotation_data


gt_euler = read_rotation_data('data/rotation/Viscam-W/10d_rotating_front/gt_euls.csv')

est_euler = read_data_from_csv('data/rotation/Viscam-W/10d_rotating_front/Mk6_Eul_res.csv')

# gt_euler = read_rotation_data('data/rotation/Viscam-W/10d_rotating_front_test/gt_euls.csv')

# est_euler = read_data_from_csv('data/rotation/Viscam-W/10d_rotating_front_test/Mk6_Eul_res.csv')



angle =  np.array([item[1] for item in gt_euler])
gt_yaw = np.array([item[4] for item in gt_euler])
gt_pitch = np.array([item[3] for item in gt_euler])
gt_roll = np.array([item[2] for item in gt_euler])
data_yaw = np.array([item[3] for item in est_euler])  # X error from eul_error (2nd column)
data_pitch = np.array([item[2] for item in est_euler])
data_roll = np.array([item[1] for item in est_euler])


gt_roll[19:54] += np.pi
gt_pitch[19:54] -= np.pi
gt_yaw[19:54] += np.pi

# print(gt_roll)
# print(gt_pitch)
# gt_pitch[gt_pitch < 0] = 2*np.pi + gt_pitch[gt_pitch < 0]
# data_pitch[data_pitch < 0] = 2*np.pi + data_pitch[data_pitch < 0]

gt_yaw[gt_yaw < 0] = 2*np.pi + gt_yaw[gt_yaw < 0]
data_yaw[data_yaw < 0] = 2*np.pi + data_yaw[data_yaw < 0]

gt_roll[gt_roll < 0] = 2*np.pi + gt_roll[gt_roll < 0]
data_roll[data_roll < 0] = 2*np.pi + data_roll[data_roll < 0]



gt_yaw = gt_yaw * 180 / np.pi
gt_pitch = gt_pitch * 180 / np.pi
gt_roll = gt_roll * 180 / np.pi
data_yaw = data_yaw * 180 / np.pi
data_pitch = data_pitch * 180 / np.pi
data_roll = data_roll * 180 / np.pi




# gt_pitch += 180
# gt_yaw += 180
# gt_roll += 180

################# X ERROR ##################
# Create a scatter plot 
plt.figure(1, figsize=(10, 4))
plt.grid(True, zorder=1)
plt.scatter(angle, gt_yaw, c='red', label='Ground Truth', alpha=0.6)
plt.scatter(angle, data_yaw, c='blue', label='X estimate', alpha=0.6)
# plt.scatter(-80, 260, color='blue', marker='x', linewidths=1)
# plt.scatter(80, 100, color='blue', marker='x', linewidths=1)
plt.xlabel('Roll (Z) Rotation [°]')
plt.ylabel('Euler Angle Yaw (X) [°]')
plt.title('Euler Angle Yaw (X) ground truth and estimate comparison')
plt.xlim(-5, 360)
plt.grid(True)
plt.legend()


################# Y ERROR ##################
# Create a scatter plot 
plt.figure(2, figsize=(10, 4))
plt.grid(True, zorder=1)
plt.scatter(angle, gt_pitch, c='red', label='Ground Truth', alpha=0.6)
plt.scatter(angle, data_pitch, c='blue', label='Y estimate', alpha=0.6)
# plt.scatter(-80, 0, color='blue', marker='x', linewidths=1)
# plt.scatter(80, 0, color='blue', marker='x', linewidths=1)
plt.xlabel('Roll (Z) Rotation [°]')
plt.ylabel('Euler Angle Pitch (Y) [°]')
plt.title('Euler Angle Pitch (Y) ground truth and estimate comparison')
plt.xlim(-5, 360)
plt.grid(True)
plt.legend()

################# Z ERROR ##################
# Create a scatter plot 
plt.figure(3, figsize=(10, 4))
plt.grid(True, zorder=1)
plt.scatter(angle, gt_roll, c='red', label='Ground Truth', alpha=0.6)
plt.scatter(angle, data_roll, c='blue', label='Z estimate', alpha=0.6)
# plt.scatter(-80, 0, color='blue', marker='x', linewidths=1)
# plt.scatter(80, 0, color='blue', marker='x', linewidths=1)
plt.xlabel('Roll (Z) Rotation [°]')
plt.ylabel('Euler Angle Roll (Z) [°]')
plt.title('Euler Angle Roll (Z) ground truth and estimate comparison')
plt.xlim(-5, 360)
plt.grid(True)
plt.legend()


plt.show()



