import numpy as np

def estimate_deviation(file_path, set_azimuth, set_elevation):
    try:
        with open(file_path, 'r') as file:
            # Read data from the file into a list of tuples (azimuth, elevation)
            data = [tuple(map(float, line.strip().split())) for line in file.readlines()]

        # Calculate deviations for azimuth and elevation
        deviations_azimuth = [azimuth - set_azimuth for azimuth, _ in data]
        deviations_elevation = [elevation - set_elevation for _, elevation in data]
        
        # Extract azimuth and elevation values
        azimuth_values = [azimuth for azimuth, _ in data]
        elevation_values = [elevation for _, elevation in data]

        # Calculate average values
        avg_azimuth = np.mean(azimuth_values)
        avg_elevation = np.mean(elevation_values)

        # Calculate standard deviations
        stddev_azimuth = np.std(deviations_azimuth)
        stddev_elevation = np.std(deviations_elevation)

        # Calculate average deviations
        avg_deviation_azimuth = sum(deviations_azimuth) / len(deviations_azimuth)
        avg_deviation_elevation = sum(deviations_elevation) / len(deviations_elevation)

        print(f"Set Azimuth: {set_azimuth}")
        print(f'Average Azimuth: {avg_azimuth}')
        print(f"Average Azimuth Deviation: {avg_deviation_azimuth}")
        print(f"Standard Azimuth Deviation: {stddev_azimuth}")
        print(f"Azimuth Deviations: {deviations_azimuth}")

        print(f"\nSet Elevation: {set_elevation}")
        print(f'Average Elevation: {avg_elevation}')
        print(f"Average Elevation Deviation: {avg_deviation_elevation}")
        print(f"Standard Elevation Deviation: {stddev_elevation}")
        print(f"Elevation Deviations: {deviations_elevation}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError:
        print("Error: Data in the file is not numerical or does not have two columns.")

# Replace 'your_file.txt' with the actual path to your text file
file_path = '60h15d.txt'

# Replace set_azimuth and set_elevation with the desired set values
set_azimuth = 173.0
set_elevation = 20.80

# Call the function
estimate_deviation(file_path, set_azimuth, set_elevation)
