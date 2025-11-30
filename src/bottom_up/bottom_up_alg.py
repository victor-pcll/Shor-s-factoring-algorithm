from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def bottom_up(a, b, N, verbose=False):
    num_qubits = N.bit_length()
    result = QuantumRegister(num_qubits, 'result')
    c = ClassicalRegister(num_qubits, 'c')
    qc = QuantumCircuit(result, c, name="mod_exp_bottom_up")

    # Initialiser result = 1
    qc.x(result[0])
    current_base = a % N

    # Exponentiation par squaring simulée
    for i in range(b.bit_length()):
        if (b >> i) & 1:
            for j in range(num_qubits):
                if (current_base >> j) & 1:
                    qc.x(result[j])
        current_base = (current_base * current_base) % N

    qc.measure(result, c)

    if verbose:
        print(qc.draw('text'))
    return qc
