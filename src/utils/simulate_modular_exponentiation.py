from qiskit_aer import AerSimulator
from qiskit import transpile

def simulate_modular_exponentiation(qc, verbose=False):
    simulator = AerSimulator()
    qc_transpiled = transpile(qc, simulator)
    job = simulator.run(qc_transpiled, shots=1)
    result = job.result()
    counts = result.get_counts()
    measured_bin = list(counts.keys())[0]
    measured_dec = int(measured_bin, 2)
    return counts, measured_bin, measured_dec, qc