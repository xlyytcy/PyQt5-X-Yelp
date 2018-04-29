from costCalulator import Y, predictions
import pickle
import os.path
import numpy as np

file_path1 = '/Users/XG/.venv/YelpxPython/Y_df.pkl'
n_bytes = 2 ** 31
max_bytes = 2 ** 31 - 1
data = bytearray(n_bytes)

bytes_in = bytes_in2 = bytearray(0)
input_size = os.path.getsize(file_path1)
with open(file_path1, 'rb') as f_in:
    for _ in range(0, input_size, max_bytes):
        bytes_in += f_in.read(max_bytes)
#Y = pickle.loads(bytes_in)

np.save('/Users/XG/.venv/YelpxPython/predic_df.pkl.npy', predictions)
#predictions = np.load('/Users/XG/.venv/YelpxPython/predic_df.pkl.npy')

