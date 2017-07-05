import json
import subprocess
import re

# FOR MONERO GPU AMD

num_gpus = 6
rig_name = "Miketheminer"
address = "USER_ADDRESS"

with open('xmr-gpu.conf', 'r') as f:
    config = json.load(f)

if len(config["Algorithms"][0]["devices"]) > num_gpus:
    for i in range(len(config["Algorithms"][0]["devices"]) - num_gpus):
        config["Algorithms"][0]["devices"].pop()

elif len(config["Algorithms"][0]["devices"]) < num_gpus:
    for i in range(num_gpus - len(config["Algorithms"][0]["devices"]), 0, -1):
        gpu = {"index": (num_gpus - i),
               "corefreq": 500,
               "memfreq": 1500,
               "fanspeed": 65,
               "powertune": 20,
               "threads": 1,
               "rawintensity": 640,
               "worksize": 16
               }
        config["Algorithms"][0]["devices"].append(gpu)

config["Algorithms"][0]["name"] = rig_name

for i in range(5):
    config["Algorithms"][0]["pools"][i]["user"] = address

with open('xmr-gpu.conf', 'w') as f:
    json.dump(config, f, indent=4, sort_keys=True)


# FOR MONERO GPU

proc = subprocess.Popen('WMIC CPU Get NumberOfCores,NumberOfLogicalProcessors /Format:List', stdout=subprocess.PIPE, shell=True)


num_threads = (proc.communicate()[0]).decode('utf-8').split()[-1].strip()
re.match(r"[0-9]+$", num_threads)
print(int(num_threads))

with open('xmr-cpu.conf', 'r') as f:
    config = json.load(f)

config["Algorithms"][0]["name"] = rig_name

for i in range(5):
    config["Algorithms"][0]["pools"][i]["user"] = address

config["Algorithms"][0]["devices"][0]["threads"] = int(num_threads) - 1

with open('xmr-cpu.conf', 'w') as f:
    json.dump(config, f, indent=4, sort_keys=True)

