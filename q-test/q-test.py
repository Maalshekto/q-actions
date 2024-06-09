import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit import QuantumCircuit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import os

res = os.getenv("QISKIT_IBM_TOKEN")
if res is None:
    print("No token provided in the environment variable QISKIT_IBM_TOKEN. Exiting.")
    exit(1)

service = QiskitRuntimeService(channel="ibm_quantum", token=os.getenv("QISKIT_IBM_TOKEN"))


from qiskit_ibm_runtime import QiskitRuntimeService

# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.h(0)
example_circuit.measure_all()
 
# backend = service.least_busy(operational=True, simulator=False)

# Transpile for simulator
simulator = AerSimulator()
example_circuit = transpile(example_circuit, simulator)

result = simulator.run(example_circuit).result()
counts = result.get_counts(example_circuit)

print(counts)
 
#sampler = Sampler(backend)
#job = sampler.run([example_circuit])
#print(f"job id: {job.job_id()}")
#result = job.result()
#print(result)