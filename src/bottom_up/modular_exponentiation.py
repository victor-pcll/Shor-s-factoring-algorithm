from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def modular_exponentiation(num_qubits, a_value=2, b_value=3, N=7, verbose=True):
    """
    Version simplifiée et fonctionnelle de a^b mod N
    utilisant un registre result unique.
    """
    result = QuantumRegister(num_qubits, 'result')
    c = ClassicalRegister(num_qubits, 'c')
    qc = QuantumCircuit(result, c, name="mod_exp_simple")

    # Initialiser result = 1
    qc.x(result[0])

    # Current_base
    current_base = a_value % N

    for i in range(num_qubits):
        if (b_value >> i) & 1:
            # Ajouter current_base au résultat bit par bit (similaire à l'addition simple)
            for j in range(num_qubits):
                if (current_base >> j) & 1:
                    qc.x(result[j])

        # Carré de la base modulo N
        current_base = (current_base * current_base) % N

    qc.measure(result, c)

    if verbose:
        print(qc.draw('text'))

    return qc