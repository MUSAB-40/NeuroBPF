# data_preprocessing.py

import pandas as pd
import numpy as np
import os

# Load execve events
execve_df = pd.read_csv('../ebpf/execve_events.log', header=None, names=['timestamp', 'pid', 'uid', 'comm', 'filename'])
execve_df['event'] = 'execve'

# Load openat events
openat_df = pd.read_csv('../ebpf/openat_events.log', header=None, names=['timestamp', 'pid', 'uid', 'comm', 'filename', 'flags'])
openat_df['event'] = 'openat'

# Load other syscall events
other_syscalls_df = pd.read_csv('../ebpf/other_syscalls_events.log', header=None, names=['timestamp', 'pid', 'uid', 'comm', 'syscall'])
other_syscalls_df['event'] = other_syscalls_df['syscall']

# Combine all events
data = pd.concat([execve_df, openat_df, other_syscalls_df], ignore_index=True)

# Ensure timestamps are numeric
data['timestamp'] = pd.to_numeric(data['timestamp'], errors='coerce')  # Convert to numeric, non-numeric to NaN

# Filter out invalid timestamps
# Valid Unix timestamp range: 0 to 2**31 (2038-01-19)
data = data[(data['timestamp'] >= 0) & (data['timestamp'] < 2**31)]

# Convert valid timestamps to datetime
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s', errors='coerce')

# Drop rows where timestamp conversion failed
data = data.dropna(subset=['timestamp'])

# Feature Engineering
# Count events per process
event_counts = data.groupby(['pid', 'event']).size().unstack(fill_value=0).reset_index()

# Labeling
# Randomly assign labels for demonstration purposes
event_counts['label'] = np.random.choice([0, 1], size=len(event_counts))  # 0: Normal, 1: Malicious

# Save preprocessed data
event_counts.to_csv('../data/preprocessed_data.csv', index=False)

print("Preprocessing complete. Data saved to '../data/preprocessed_data.csv'")
