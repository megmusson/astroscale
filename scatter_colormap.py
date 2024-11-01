import numpy as np
import matplotlib.pyplot as plt
import csv
from functions import read_data_from_csv
from plot_xy_error import plot_error
from plot_detected import plot_detection_results
# import functions

############ READ FILE ################
# XY Error at
tvec_error = read_data_from_csv('data/Viscam-W_random/15d_xy_error_0.25distribution/Mk6_Tvec_err.csv')
gt_tvec_err = read_data_from_csv('data/Viscam-W_random/15d_xy_error_0.25distribution/gt_tvecs.csv')

# tvec_1d = read_data_from_csv('data/distance/W/10d_random_xy_const_z/Mk6_Tvec_err.csv')
tvec_1d = read_data_from_csv('data/distance/W/subpixel_refinement/10d_random_xy_const_z/Mk6_Tvec_err.csv')
gt_tvec_1d = read_data_from_csv('data/distance/W/10d_random_xy_const_z/gt_tvecs.csv')


# Detected or not at 3.5m
tvec_res_35d = read_data_from_csv('data/Viscam-W_random/3.5d_xy_error/Mk6_Tvec_res.csv')
gt_tvec_res_35d = read_data_from_csv('data/Viscam-W_random/3.5d_xy_error/gt_tvecs.csv')
# Detected or not at 4m, dark splot light
tvec_res_40d = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8distribution/Mk6_Tvec_res.csv')
gt_tvec_res_40d = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8distribution/gt_tvecs.csv')
# Detected or not at 4m, constant sunlight lighting slight angle - medium bright
tvec_res_40d_cs = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8dist_sunlight/Mk6_Tvec_res.csv')
gt_tvec_res_40d_cs = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8dist_sunlight/gt_tvecs.csv')
# Detected or not at 4m, constant sunlight lighting 90 angle - dark
tvec_res_40d_cs_side = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8dist_sunside/Mk6_Tvec_res.csv')
gt_tvec_res_40d_cs_side = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8dist_sunside/gt_tvecs.csv')

# Detected or not at 4m, concentrated spotlight
tvec_res_40d_sp = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8_spotlight/Mk6_Tvec_res.csv')
gt_tvec_res_40d_sp = read_data_from_csv('data/Viscam-W_random/40d_random_xy_const_z_0.8_spotlight/gt_tvecs.csv')
# Detected or not at 3m, concentrated spotlight
# tvec_res_30d_sp = read_data_from_csv('data/Viscam-W_random/30d_random_xy_const_z_0.65_spotlight/Mk6_Tvec_res.csv')
# gt_tvec_res_30d_sp = read_data_from_csv('data/Viscam-W_random/30d_random_xy_const_z_0.65_spotlight/gt_tvecs.csv')
# Detected or not at 3m, concentrated spotlight better
tvec_res_30d_sp = read_data_from_csv('data/Viscam-W_random/30d_random_xy_const_z/Mk6_Tvec_res.csv')
gt_tvec_res_30d_sp = read_data_from_csv('data/Viscam-W_random/30d_random_xy_const_z/gt_tvecs.csv')


# tvec_3d = read_data_from_csv('data/Viscam-W/30d_random_xy_const_z/Mk6_Tvec_res.csv')
# gt_tvec_3d = read_data_from_csv('data/Viscam-W/30d_random_xy_const_z/gt_tvecs.csv')

######## Main #########
if __name__ == "__main__":

    # XY Error at 1.5m distance
    # plot_error(gt_tvec_err, tvec_error, 1.5)

    # Detected or not at 3.5m, spotlight
    # plot_detection_results(gt_tvec_res_35d, tvec_res_35d, 3.5)
    # Detected or not at 4m, spotlight
    # plot_detection_results(gt_tvec_res_40d, tvec_res_40d, 4)
    # Detected or not at 4m
    # plot_detection_results(gt_tvec_res_40d_cs, tvec_res_40d_cs, 4)
    # Detected or not at 4m
    # plot_detection_results(gt_tvec_res_40d_cs_side, tvec_res_40d_cs_side, 4)
    # Detected or not at 4m spotlight concentrated
    # plot_detection_results(gt_tvec_res_40d_sp, tvec_res_40d_sp, 4)
    # Detected or not at 3m spotlight concentrated
    # plot_detection_results(gt_tvec_res_30d_sp, tvec_res_30d_sp, 3)

    # plot_error(gt_tvec_3d, tvec_3d, 3)
    # plot_detection_results(gt_tvec_3d, tvec_3d, 3)
    plot_error(gt_tvec_1d, tvec_1d, 1)




