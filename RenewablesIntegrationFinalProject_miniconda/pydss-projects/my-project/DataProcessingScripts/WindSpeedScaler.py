import pandas as pd
import os

# Define file paths
path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(path, "windspeed_data_2020-03-10.csv")
output_dir = os.path.join(path, "../DSSfiles")
output_file = os.path.join(output_dir, "windspeed_data_scaled_2020-03-10.csv")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load wind speed data
df = pd.read_csv(input_file, header=None)
# df[1] = pd.to_numeric(df[0], errors='coerce')

# Scale wind speed values
df[1] = df[1] * (15 / 8)

df.reindex(columns=[1])

print(df.head())

# Save back to CSV
df.to_csv(output_file, header=False, index=False)

print(f"File saved to {output_file}")
