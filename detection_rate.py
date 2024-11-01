import matplotlib.pyplot as plt
import numpy as np


# VISCam-W
distances_VW = [1, 2, 3, 3.5, 4, 4.5, 5, 5.5]
detection_rates_VW = [100, 100, 95, 93, 50, 44, 38, 0]
# Mean error 
x_mean_W = [-0.000338459, -0.00181347, 0.00157532, 0.00151134, -0.00400135, -0.0048387, -0.00445346]
y_mean_W = [0.000150083, -0.000221601, -0.00084192, 0.00273437, -0.0134166, 0.00234557, 0.00718577 ]
z_mean_W = [0.0158976, 0.0573265, 0.125531, 0.178944, 0.262793, 0.276395, 0.208185 ]
# sigma error
x_sigma_W = [0.0037365, 0.0121639, 0.0308286, 0.0279554, 0.0643832, 0.0531923, 0.0456555 ]
y_sigma_W = [0.00334388, 0.00969881, 0.0221365, 0.033399, 0.0504422, 0.0493611, 0.0305829]
z_sigma_W = [0.00367927, 0.0178669, 0.0653705, 0.0806152, 0.0844818, 0.013108, 0.0716097]

# with corner refinement
x_mean_W_SR = [-0.000176968, -0.000952378, 0.000771873, 0.00487592, 0.00231625, -0.0109587, -0.00383949]
y_mean_W_SR = [0.000106286, 0.000139321, 0.000105121, 0.0036569, -0.0224916, -0.00464839, 0.00730578]
z_mean_W_SR = [0.006697, 0.0395285, 0.146738, 0.34957, 0.484284, 0.203847, 0.324699]
x_sigma_W_SR = [0.0018073, 0.00755262, 0.0297621, 0.0468566, 0.11981, 0.0562851, 0.0745001]
y_sigma_W_SR = [0.00158907, 0.00691834, 0.0272972, 0.0596143, 0.0923522, 0.0610681, 0.0516865]
z_sigma_W_SR = [0.000462434, 0.00899727, 0.0325601, 0.0511959, 0.0648806, 0.247929, 0.153553]



x_mean_W_CR = [-0.000419432, 0.00118986, -0.00226247, 0.000987944, -0.00279229, -0.00180859, -0.00557484]
y_mean_W_CR = [0.000186772, -0.0014358, 3.7491e-05, 0.00221081, -0.0141604, 0.00173281, 0.00770874]
z_mean_W_CR = [0.0205959, 0.11882, 0.0549515, 0.161525,  0.241237, 0.279939, 0.184288]

x_sigma_W_CR = [0.00478997, 0.0273365, 0.0122907, 0.0234957, 0.061161, 0.0664322, 0.0382288]
y_sigma_W_CR = [0.00409828, 0.0198801, 0.00961278, 0.0284416, 0.0484719, 0.0536501, 0.025925]
z_sigma_W_CR = [0.00497389, 0.0521683, 0.0236099, 0.0608844, 0.0849882, 0.0455135, 0.0572007]



# VISCam-T
distances_VT = [1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16]
detection_rates_VT = [100, 100, 100, 100, 100, 98, 99, 82, 57, 58, 60, 29, 0]
# Mean error 
x_mean_T = [2.40017e-05, -2.86302e-05, 0.000114373, -0.000627375, 0.0015121, -0.00182915, 0.00544475, 0.00303144, -0.0101412, -0.0050666, 0.00368518, 0.00154371]
y_mean_T = [3.26681e-05, -3.43083e-05, 0.000189006, -0.00052747, -0.00133145, 0.00266791, 0.00230193, -0.00564516, -0.00764965, 0.00352351, 0.00103827, -0.00907305]
z_mean_T = [0.00483735, 0.0201412, 0.0845992, 0.135309, 0.23849, 0.337727, 0.456095, 0.521766, 0.690873, 0.808448, 0.986438, 0.580125]
# sigma error
x_sigma_T = [0.000294815, 0.00111821, 0.00483837, 0.00861836, 0.0162231, 0.0221584, 0.0351407, 0.0450392, 0.0551691, 0.0570191, 0.0678786, 0.0412572]
y_sigma_T = [0.000314062, 0.0010989, 0.0051304, 0.00916084, 0.0137124, 0.020262, 0.033206, 0.0422381, 0.0531827, 0.0529209, 0.0666995, 0.0361699]
z_sigma_T = [0.00139614, 0.00530019, 0.0196671, 0.0433212, 0.0640709, 0.0849189, 0.169399, 0.289256, 0.214061, 0.402786, 0.481303, 0.216522]

# with corner refinement
x_mean_T_SR = [1.44599e-05, 9.38617e-06, 0.00013961, -0.000504724, -7.89698e-05, -0.00159465, 0.00799151, 0.00479725, -0.0291904, -0.00141171, 0.00125887, 0.00143128]
y_mean_T_SR = [1.59416e-05, -2.01366e-05, 0.000190017, -1.29617e-05, -0.00095792, 0.00250918, 0.00426611, -0.012187, -0.0112334, 0.0053378, -0.00155246, -0.0182139]
z_mean_T_SR = [0.0022359, 0.0110885, 0.0504515, 0.0813986, 0.142106, 0.187811, 0.937413, 1.14026, 1.38023, 0.862244, 1.2327, 0.775926, ]
x_sigma_T_SR = [0.000143752, 0.000649805, 0.00286518, 0.0049218, 0.0101878, 0.0141786, 0.0677528, 0.0878347, 0.107141, 0.0819422, 0.0923363, 0.0516292]
y_sigma_T_SR = [0.000148226, 0.000608274, 0.00301183, 0.00521309, 0.00858332, 0.0110416, 0.0663239, 0.0797536, 0.0934895, 0.0690423, 0.0744586, 0.0519067]
z_sigma_T_SR = [6.93841e-05, 0.000442341, 0.00218246, 0.00590154, 0.016472, 0.0207431, 0.217541, 0.116047, 0.0506368, 0.721985, 0.45243, 0.418151]





################## DETECTION RATE ##############
fig_detection_rate = plt.figure(figsize=(10, 6))
plt.plot(distances_VT, detection_rates_VT, marker='o', linestyle='-', label='VISCam-T', color='C0')
plt.plot(distances_VW, detection_rates_VW, marker='o', linestyle='-', label='VISCam-W', color='forestgreen')
# Setting labels and title
plt.xlabel('Distance [m]')
plt.ylabel('Detection Rate [%]')
plt.title('Detection Rate Comparison using VISCam-W and VISCam-T')
# Setting x-axis to have consistent intervals
plt.xticks(range(0, 17))
plt.ylim(0, 17)
plt.ylim(0, 110)
plt.grid(True)
plt.legend()

############# W #####################
fig_xy_W = plt.figure(figsize=(12, 8))
plt.errorbar(distances_VW[:-1], x_mean_W, yerr=x_sigma_W, fmt='o-', label='X', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='forestgreen')
plt.errorbar(distances_VW[:-1], y_mean_W, yerr=y_sigma_W, fmt='s-', label='Y', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='yellowgreen')

plt.errorbar(distances_VW[:-1], x_mean_W_SR, yerr=x_sigma_W, fmt='o-', label='X - subpixel refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='red')
plt.errorbar(distances_VW[:-1], y_mean_W_SR, yerr=y_sigma_W, fmt='s-', label='Y - subpixel refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='pink')
plt.errorbar(distances_VW[:-1], x_mean_W_CR, yerr=x_sigma_W, fmt='o-', label='X - contour refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='indigo')
plt.errorbar(distances_VW[:-1], y_mean_W_CR, yerr=y_sigma_W, fmt='s-', label='Y - contour refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='slateblue')

# Customize the plot
plt.xlabel('Sample Points')
plt.ylabel('Error [m]')
plt.title('X Y Mean Translation Error with Standard Deviation - VISCam-W')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.legend()
# Add minor gridlines
plt.grid(True, which='minor', linestyle=':', alpha=0.4)
# Show the plot
plt.tight_layout()

fig_z_W = plt.figure(figsize=(12, 8))
plt.errorbar(distances_VW[:-1], z_mean_W, yerr=z_sigma_W, fmt='o-', label='Z', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='forestgreen')

plt.errorbar(distances_VW[:-1], z_mean_W_SR, yerr=z_sigma_W, fmt='o-', label='Z - subpixel refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='red')
plt.errorbar(distances_VW[:-1], z_mean_W_CR, yerr=z_sigma_W, fmt='o-', label='Z - contour refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='indigo')

# Customize the plot
plt.xlabel('Sample Points')
plt.ylabel('Error [m]')
plt.title('Z Mean Translation Error with Standard Deviation - VISCam-W')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.legend()
# Add minor gridlines
plt.grid(True, which='minor', linestyle=':', alpha=0.4)
# Show the plot
plt.tight_layout()

fig_xy_T = plt.figure(figsize=(12, 8))
plt.errorbar(distances_VT[:-1], x_mean_T, yerr=x_sigma_T, fmt='o-', label='X', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='C0')
plt.errorbar(distances_VT[:-1], y_mean_T, yerr=y_sigma_T, fmt='s-', label='Y', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='lightskyblue')

plt.errorbar(distances_VT[:-1], x_mean_T_SR, yerr=x_sigma_T, fmt='o-', label='X - subpixel refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='red')
plt.errorbar(distances_VT[:-1], y_mean_T_SR, yerr=y_sigma_T, fmt='s-', label='Y - subpixel refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6, color='pink')
# Customize the plot
plt.xlabel('Sample Points')
plt.ylabel('Error [m]')
plt.title('X Y Mean Translation Error with Standard Deviation - VISCam-T')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.legend()
# Add minor gridlines
plt.grid(True, which='minor', linestyle=':', alpha=0.4)
# Show the plot
plt.tight_layout()

fig_z_T = plt.figure(figsize=(12, 8))
plt.errorbar(distances_VT[:-1], z_mean_T, yerr=z_sigma_T, fmt='o-', label='Z', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6,  color='C0')

plt.errorbar(distances_VT[:-1], z_mean_T_SR, yerr=z_sigma_T, fmt='o-', label='Z - subpixel refinement', capsize=5, capthick=1.5, elinewidth=1.5, markersize=6,  color='red')
# Customize the plot
plt.xlabel('Sample Points')
plt.ylabel('Error [m]')
plt.title('Z Mean Translation Error with Standard Deviation - VISCam-T')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.legend()
# Add minor gridlines
plt.grid(True, which='minor', linestyle=':', alpha=0.4)
# Show the plot
plt.tight_layout()




plt.show()