from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def modular_multiplication(num_qubits, a_value=1, N=15, verbose=True):
    """
    Crée un circuit simple pour la multiplication modulaire
    (a * b) mod N en utilisant des additions modulaires répétées.

    Arguments:
        num_qubits : nombre de qubits pour les registres
        a_value : base classique à multiplier
        N : modulo classique
        verbose : si True, affiche le circuit en ASCII

    Retourne:
        QuantumCircuit
    """
    # Registres
    b = QuantumRegister(num_qubits, 'b')       # opérande
    result = QuantumRegister(num_qubits, 'result')  # accumule le produit
    c = ClassicalRegister(num_qubits, 'c')     # pour la mesure

    qc = QuantumCircuit(b, result, c, name="mod_mul_simple")

    # Initialiser le résultat à 0 (par défaut tous les qubits sont à 0)
    # On pourrait initialiser à 1 si nécessaire avec qc.x(result[0])

    # Répéter pour chaque bit de b (addition modulaire)
    for i in range(num_qubits):
        # Si le bit b[i] est 1, ajouter (a_value << i) mod N au résultat
        shift = (a_value * (2 ** i)) % N
        # Initialiser un registre temporaire pour la constante
        temp = QuantumRegister(num_qubits, f'temp_{i}')
        qc.add_register(temp)
        # Initialiser temp avec la valeur shift
        for j in range(num_qubits):
            if (shift >> j) & 1:
                qc.x(temp[j])
        # Addition modulaire simple : result += temp
        for j in range(num_qubits):
            qc.cx(temp[j], result[j])
            if j > 0:
                qc.cx(temp[j-1], result[j])

    # Mesurer le résultat
    qc.measure(result, c)

    if verbose:
        print(qc.draw('text'))

    return qc