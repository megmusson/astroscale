import cv2
import importlib
import numpy as np 
from scipy.spatial.transform import Rotation
import matplotlib.pyplot as plot

# 1 [m]
# vals = np.loadtxt("data/distance/W/10d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")
# gt_tvec = np.loadtxt("data/distance/W/10d_random_xy_const_z/gt_tvecs.csv",delimiter=",")
# vals = np.loadtxt("data/distance/W/subpixel_refinement/10d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")

# 2 [m]
# vals = np.loadtxt("data/distance/W/20d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")
# gt_tvec = np.loadtxt("data/distance/W/20d_random_xy_const_z/gt_tvecs.csv",delimiter=",")
# vals = np.loadtxt("data/distance/W/subpixel_refinement/20d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")

# 3 [m]
# vals = np.loadtxt("data/distance/W/30d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")
# gt_tvec = np.loadtxt("data/distance/W/30d_random_xy_const_z/gt_tvecs.csv",delimiter=",")
# vals = np.loadtxt("data/distance/W/subpixel_refinement/30d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")

# 5 [m]
vals = np.loadtxt("data/distance/W/50d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")
gt_tvec = np.loadtxt("data/distance/W/50d_random_xy_const_z/gt_tvecs.csv",delimiter=",")
# vals = np.loadtxt("data/distance/W/subpixel_refinement/50d_random_xy_const_z/Mk6_Rvec_res.csv",delimiter=",")


R_ref= np.array([[1,0,0],
       [0,-1,0],
       [0,0,-1]])


# Create a set of detected image numbers for easy lookup
detected_images_index = set(int(row[0]) for row in vals)
print(detected_images_index)
print(len(detected_images_index))
# Separate ground truth into detected and undetected - mask is array of true or false
detected_mask = np.array([int(i[0]) in detected_images_index for i in gt_tvec]) ## -1 if results start with index 0
print(detected_mask)
gt_detected = np.array(gt_tvec[detected_mask])
# not_detected_mask = ~detected_mask
# not_detected = np.array(gt[1:])[not_detected_mask]
print("index ", gt_detected[:,0])
x = gt_detected[:,1]
y = gt_detected[:,2]


results_euler_int = []
for val in vals:
    R = cv2.Rodrigues(val[1:4])[0]
    results_euler_int.append(np.degrees((Rotation.from_matrix(R@R_ref.T).as_euler("YXZ"))))
    # results_euler_int.append(np.degrees((Rotation.from_matrix(R@R_ref.T).as_euler("XYZ"))))
    # results_euler_int.append(np.degrees((Rotation.from_matrix(R@R_ref.T).as_euler("ZYX"))))
results_euler_int = np.array(results_euler_int)

roll_error = results_euler_int[:,2]      # Z
yaw_error = results_euler_int[:,0]    # Y
pitch_error = results_euler_int[:,1]     # X

# pitch_error = results_euler_int[:,2]
# yaw_error = results_euler_int[:,1]
# roll_error = results_euler_int[:,0]

# roll_error = results_euler_int[:,0]
# yaw_error = results_euler_int[:,1]
# pitch_error = results_euler_int[:,2]


# # PRINT RESULTS 

robust_mean = np.median(results_euler_int,axis=0) 
robust_std  = np.median(np.abs(results_euler_int-np.median(results_euler_int,axis=0)),axis=0)*1.468
robust_rms  = np.sqrt(robust_mean**2+robust_std**2)
total_error = np.sqrt(np.sum(robust_mean**2+robust_std**2))

print("robust mean degree [%.2f, %.2f, %.2f]"%tuple(robust_mean))
print("robust std degree  [%.2f, %.2f, %.2f]"%tuple(robust_std))
print("robust rms degree  [%.2f, %.2f, %.2f]"%tuple(robust_rms))

print("robust total error degree  %.2f"%total_error)

print("means degree",results_euler_int.mean(axis=0))
print("stds degree",results_euler_int.std(axis=0))
print("rms degree",np.sqrt(results_euler_int.std(axis=0)**2+results_euler_int.mean(axis=0)**2))
print("Total error",np.sqrt(np.sum(results_euler_int.std(axis=0)**2+results_euler_int.mean(axis=0)**2)))

roll_all_max = np.max(np.abs(roll_error))
yaw_all_max = np.max(np.abs(yaw_error))
pitch_all_max = np.max(np.abs(pitch_error))

# Define the valid range
min_val, max_val = -10, 10
# min_val, max_val = -2, 2
roll_in_range = (roll_error >= min_val) & (roll_error <= max_val)
roll_out_of_range = ~roll_in_range
roll_max = np.max(np.abs(roll_error[roll_in_range]))
yaw_in_range = (yaw_error >= min_val) & (yaw_error <= max_val)
yaw_out_of_range = ~yaw_in_range
yaw_max = np.max(np.abs(yaw_error[yaw_in_range]))
pitch_in_range = (pitch_error >= min_val) & (pitch_error <= max_val)
pitch_out_of_range = ~pitch_in_range
pitch_max = np.max(np.abs(pitch_error[pitch_in_range]))
print(roll_max)
print(yaw_max)
print(pitch_max)

f1 = plot.figure(1, figsize=(8.18, 6.1))
plot.scatter(x[roll_in_range], y[roll_in_range], c=roll_error[roll_in_range], cmap='PuOr', vmin=-roll_max, vmax=roll_max, s=70, edgecolor='gray', linewidth=0.1)
cbar = plot.colorbar()
cbar.set_label('Roll Error [degrees]')
plot.scatter(x[roll_out_of_range], y[roll_out_of_range], color='white', edgecolor='gray', linewidth=0.5, s=70, label='Out of Range')
plot.xlabel("X Position")
plot.ylabel("Y Position")
plot.title("Roll Error with respect to marker position - Outliers removed ±10°")
plot.legend()

f2 = plot.figure(2, figsize=(8.18, 6.1))
plot.scatter(x[yaw_in_range], y[yaw_in_range], c=yaw_error[yaw_in_range], cmap='PuOr', vmin=-yaw_max, vmax=yaw_max, s=70, edgecolor='gray', linewidth=0.1,)
cbar = plot.colorbar()
cbar.set_label('Yaw Error [degrees]')
plot.scatter(x[yaw_out_of_range], y[yaw_out_of_range], color='white', edgecolor='gray', linewidth=0.5, s=70, label='Out of Range')
plot.xlabel("X Position")
plot.ylabel("Y Position")
plot.title("Yaw Error with respect to marker position - Outliers removed ±10°")
plot.legend()

f3 = plot.figure(3, figsize=(8.18, 6.1))
plot.scatter(x[pitch_in_range], y[pitch_in_range], c=pitch_error[pitch_in_range], vmin=-pitch_max, vmax=pitch_max, cmap='PuOr', s=70, edgecolor='gray', linewidth=0.1,)
cbar = plot.colorbar()
cbar.set_label('Pitch Error [degrees]')
plot.scatter(x[pitch_out_of_range], y[pitch_out_of_range], color='white', edgecolor='gray', linewidth=0.5, s=70, label='Out of Range')
plot.xlabel("X Position")
plot.ylabel("Y Position")
plot.title("Pitch Error with respect to marker position - Outliers removed ±10°")
plot.legend()


f4 = plot.figure(4, figsize=(8.18, 6.1))
plot.scatter(x, y, c=roll_error, cmap='PuOr', vmin=-roll_all_max, vmax=roll_all_max, s=70, edgecolor='gray', linewidth=0.1,)
cbar = plot.colorbar()
cbar.set_label('Roll Error [degrees]')
plot.xlabel("X Position")
plot.ylabel("Y Position")
plot.title("Roll Error with respect to marker position")
# plot.legend()

f5 = plot.figure(5, figsize=(8.18, 6.1))
plot.scatter(x, y, c=yaw_error, cmap='PuOr', vmin=-yaw_all_max, vmax=yaw_all_max, s=70, edgecolor='gray', linewidth=0.1,)
cbar = plot.colorbar()
cbar.set_label('Yaw Error [degrees]')
plot.xlabel("X Position")
plot.ylabel("Y Position")
plot.title("Yaw Error with respect to marker position")
# plot.legend()

f6 = plot.figure(6, figsize=(8.18, 6.1))
plot.scatter(x, y, c=pitch_error, cmap='PuOr', vmin=-pitch_all_max, vmax=pitch_all_max, s=70, edgecolor='gray', linewidth=0.1,)
cbar = plot.colorbar()
cbar.set_label('Pitch Error [degrees]')
plot.xlabel("X Position")
plot.ylabel("Y Position")
plot.title("Pitch Error with respect to marker position")
# plot.legend()

f7 = plot.figure(7)
plot.plot(roll_error, label = "roll error")
plot.plot(yaw_error, label = "yaw error")
plot.plot(pitch_error, label = "pitch error")
plot.title("Euler error comparison at 5[m] distance with intrinsic YXZ")
plot.legend()
plot.xlabel("sample id")
plot.ylabel("degree")
# plot.ylim(-40,40)
plot.show()






