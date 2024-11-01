import numpy as np
import matplotlib.pyplot as plt
import csv

def read_data_from_csv(filename):
    data = []
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the first line (header)
        next(csv_reader)
        
        # Read data until we encounter "Summary"
        for row in csv_reader:
            # If we encounter "Summary", stop reading
            if row[0].startswith('Summary'):
            # if row[0].strip().lower() == "Summary:":
                break
            
            # Convert the first column to an integer (image number), the rest to floats
            image_number = int(row[0])
            x = float(row[1])
            y = float(row[2])
            z = float(row[3])
            
            # Append to the list as a tuple (image_number, dx, dy, dz)
            data.append((image_number, x, y, z))
    
    return data


def read_rotation_data(filename):
    data = []
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the first line (header)
        next(csv_reader)
        
        # Read data until we encounter "Summary"
        for row in csv_reader:
            # If we encounter "Summary", stop reading
            if row[0].startswith('Summary'):
            # if row[0].strip().lower() == "Summary:":
                break
            
            # Convert the first column to an integer (image number), the rest to floats
            image_number = int(row[0])
            angle = int(row[1])
            x = float(row[2])
            y = float(row[3])
            z = float(row[4])

            # print("x: ", x)
            # print("y: ", y)
            
            # Append to the list as a tuple (image_number, dx, dy, dz)
            data.append((image_number, angle, x, y, z))
    
    return data


def distance_to_fov(distance):

    T_distance_table = np.array([
                        [1, 0.199, 0.149],
                        [2, 0.398, 0.297],
                        [3, 0.597, 0.446],
                        [3.5, 0.697, 0.520],
                        [4, 0.797, 0.594],
                        [5, 0.996, 0.743],
                        [6, 1.194, 0.888],
                        [7, 1.393, 1.036],
                        [8, 1.592, 1.184],
                        [9, 1.791, 1.332],
                        [10, 1.990, 1.480],
                        [11, 2.189, 1.628],
                        [12, 2.388, 1.776]
                    ])
    
    W_distance_table = np.array([
        [1, 0.60, 0.45],
        [1.5, 0.9, 0.674],
        [2, 1.20, 0.90],
        [3, 1.80, 1.35],
        [3.5, 2.10, 1.57],
        [4, 2.40, 1.80],
        [5, 3.00, 2.25]
    ])
    
    for row in W_distance_table:
        if row[0] == distance:
            return row[1], row[2]
        
    return None



