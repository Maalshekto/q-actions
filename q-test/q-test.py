import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit import QuantumCircuit
import os

res = os.getenv("QISKIT_IBM_TOKEN")
if res is None:
    print("No token provided in the environment variable QISKIT_IBM_TOKEN. Exiting.")
    exit(1)

service = QiskitRuntimeService(channel="ibm_quantum", token=os.getenv("QISKIT_IBM_TOKEN"))


from qiskit_ibm_runtime import QiskitRuntimeService

# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()
 
backend = service.least_busy(operational=True, simulator=False)
 
sampler = Sampler(backend)
job = sampler.run([example_circuit])
print(f"job id: {job.job_id()}")
result = job.result()
print(result)