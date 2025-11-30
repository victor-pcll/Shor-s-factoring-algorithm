from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def modular_add(num_qubits, constant=0, verbose=True):
    """
    Crée un circuit quantique simple pour addition modulaire
    entre un registre 'a' et une constante 'constant'.

    Arguments:
        num_qubits : nombre de qubits pour les registres
        constant : valeur classique à ajouter
        verbose : si True, affiche le circuit en ASCII

    Retourne:
        QuantumCircuit
    """
    # Registres
    a = QuantumRegister(num_qubits, 'a')
    b = QuantumRegister(num_qubits, 'b')
    c = ClassicalRegister(num_qubits, 'c')

    qc = QuantumCircuit(a, b, c, name="mod_add_simple")

    # Initialiser b avec la constante
    for i in range(num_qubits):
        if (constant >> i) & 1:
            qc.x(b[i])

    # Addition mod 2^n (réversible)
    for i in range(num_qubits):
        qc.cx(a[i], b[i])
        if i > 0:
            qc.cx(a[i-1], b[i])

    # Mesurer le résultat
    qc.measure(b, c)

    # Affichage si verbose
    if verbose:
        print(qc.draw('text'))

    return qc