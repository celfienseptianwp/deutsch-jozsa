# ========================
# Deutsch-Jozsa Algorithm
# ========================
def deutsch_jozsa(circuit, oracle, n_qubit):
    # Initialize the ancilla qubit
    circuit.x(n_qubit - 1)
    circuit.h(n_qubit - 1)
    circuit.barrier()

    # H-gate for each input qubits
    circuit.h(range(n_qubit - 1))

    # Apply any oracle
    circuit.append(oracle, range(n_qubit))

    # H-gate again for each input qubits
    circuit.h(range(n_qubit - 1))
    circuit.barrier()

   