import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService
import os

res = os.getenv("QISKIT_IBM_TOKEN")
if res is None:
    print("No token provided in the environment variable QISKIT_IBM_TOKEN. Exiting.")
    exit(1)

service = QiskitRuntimeService(channel="ibm_quantum", token=os.getenv("QISKIT_IBM_TOKEN"))