# NeuroBPF
 Malware Detection using Machine Learning with eBPF for Linux

## Setup Instructions

### Prerequisites

- Linux system with kernel version >= 4.9
- Python 3.x
- Root privileges for running eBPF scripts

### Install Dependencies
```bash
sudo apt-get update
sudo apt-get install -y python3-pip linux-headers-$(uname -r) build-essential
sudo apt-get install -y bpfcc-tools libbpfcc-dev linux-tools-common linux-tools-$(uname -r)
sudo apt install git -y
git clone https://github.com/ammark11/NeuroBPF
cd NeuroBPF
pip3 install -r requirements.txt
```
### For externally-managed-environment
Use a Virtual Environment:
Step 1: Create a Virtual Environment
```bash
python3 -m venv venv
```
Step 2: Activate the Virtual Environment
```bash
source venv/bin/activate
```
Step 3: Install Dependencies
```bash
pip3 install -r requirements.txt
```
Step 4: Deactivate When Done
```bash
deactivate
```

### Usage
Step 1: Data Collection with eBPF
Navigate to the ebpf/ directory and run the eBPF scripts with root privileges.
```bash
cd ebpf
sudo python3 execve_trace.py & sudo python3 open_trace.py & sudo python3 other_syscall_traces.py
```
---> The scripts will generate log files (*.log) in the same directory.

Step 2: Data Preprocessing
Navigate to the ml/ directory and preprocess the collected data.
```bash
cd ../ml
python3 data_preprocessing.py
```
Step 3: Model Training
Train the machine learning model using the preprocessed data.
```bash
python3 train_model.py
```
Step 4: Model Evaluation
Evaluate the trained model and view the results.
```bash
python3 evaluate_model.py
```
Step 5: Making Predictions
Use the trained model to make predictions on new data.
```bash
python3 predict.py
```
