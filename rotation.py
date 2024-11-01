
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the ground truth and result files, skipping the first line as it's a header
ground_truth = pd.read_csv('data/Viscam-W/20d_rotating_hor/gt_euls.csv', skiprows=1, header=None, names=['image_number', 'angle', 'x', 'y', 'z'])
result = pd.read_csv('data/Viscam-W/20d_rotating_hor/Mk6_Rvec_res.csv', skiprows=1, header=None, names=['image_number', 'x', 'y', 'z'])

# Subtract pi from every value in the result y column
# result['y'] = result['y'] - np.pi

# Ensure image_number is treated as integers after skipping the title row
result['image_number'] = pd.to_numeric(result['image_number'], errors='coerce')
result = result.dropna(subset=['image_number'])
result['image_number'] = result['image_number'].astype(int)

# Create a list of angles from -80 to +85 with a step of 5
angles = list(range(-80, 86, 5))

# Map the image_number to corresponding angles in the result file
result['angle'] = result['image_number'].apply(lambda num: angles[num - 1])

# Identify missing image_numbers (from 1 to 33)
all_image_numbers = set(range(1, 34))  # Assuming image numbers are from 1 to 33
detected_image_numbers = set(result['image_number'])
missing_image_numbers = all_image_numbers - detected_image_numbers

# Create a DataFrame for missing entries
missing_data = pd.DataFrame({
    'image_number': list(missing_image_numbers),
    'angle': [angles[num - 1] for num in missing_image_numbers],
    'x': [0] * len(missing_image_numbers),  # Set y-value to 0 for undetected
    'y': [0] * len(missing_image_numbers),   # Set y-value to 0 for undetected
    'z': [0] * len(missing_image_numbers)   # Set y-value to 0 for undetected
})


# Plot result x values against angles
plt.figure(1, figsize=(10, 6))
# Plot detected points
plt.plot(result['angle'], result['y'], marker='o', linestyle='-', color='darkblue', label='Result X vs Angle')
# Plot ground truth y values
plt.plot(ground_truth['angle'], ground_truth['y'], marker='s', linestyle='--', color='orange', label='Ground Truth Y vs Angle')
# Plot missing points
plt.scatter(missing_data['angle'], missing_data['y'], color='darkred', label='Missing Detection', zorder=5)
# Customize the plot
plt.title('Y values from Result vs Angle')
plt.xlabel('Angle (degrees)')
plt.ylabel('Y value')
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')  # Add a horizontal line at y=0
plt.legend()
plt.grid(True)

# Plot result x values against angles
plt.figure(2, figsize=(10, 6))
# Plot detected points
plt.plot(result['angle'], result['x'], marker='o', linestyle='-', color='darkblue', label='Result X vs Angle')
# Plot ground truth y values
plt.plot(ground_truth['angle'], ground_truth['x'], marker='s', linestyle='--', color='orange', label='Ground Truth Y vs Angle')
# Plot missing points
plt.scatter(missing_data['angle'], missing_data['x'], color='darkred', label='Missing Detection', zorder=5)
# Customize the plot
plt.title('X values from Result vs Angle')
plt.xlabel('Angle (degrees)')
plt.ylabel('X value')
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')  # Add a horizontal line at y=0
plt.legend()
plt.grid(True)


# Plot result x values against angles
plt.figure(3, figsize=(10, 6))
# Plot detected points
plt.plot(result['angle'], result['z'], marker='o', linestyle='-', color='darkblue', label='Result X vs Angle')
# Plot ground truth y values
plt.plot(ground_truth['angle'], ground_truth['z'], marker='s', linestyle='--', color='orange', label='Ground Truth Y vs Angle')
# Plot missing points
plt.scatter(missing_data['angle'], missing_data['z'], color='darkred', label='Missing Detection', zorder=5)
# Customize the plot
plt.title('Z values from Result vs Angle')
plt.xlabel('Angle (degrees)')
plt.ylabel('Z value')
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')  # Add a horizontal line at y=0
plt.legend()
plt.grid(True)


plt.show()



