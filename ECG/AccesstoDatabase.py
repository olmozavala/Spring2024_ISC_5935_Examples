# %%
import wfdb

# Define the path to your HEA (header) file
hea_file_path = './Data/200'

# Read the header file
record = wfdb.rdheader(hea_file_path)

# Now readthe annotation file
annotation = wfdb.rdann(hea_file_path, 'atr')

# Print the header information
print(record.__dict__)


x = 1