from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def compiled_algorithm(a, b, N, num_qubits, verbose=False):
    result_value = pow(a, b, N)

    result = QuantumRegister(num_qubits, 'result')
    c = ClassicalRegister(num_qubits, 'c')
    qc = QuantumCircuit(result, c, name="mod_exp_compiled")

    for i in range(num_qubits):
        if (result_value >> i) & 1:
            qc.x(result[i])
    qc.measure(result, c)

    if verbose:
        print(qc.draw('text'))

    return qc