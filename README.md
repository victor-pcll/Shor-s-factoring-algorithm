# Project 7 - Shor’s factoring algorithm

This repository contains an implementation of **Shor’s algorithm** for integer factorization, designed to run on IBM’s Qiskit platform using the QASM simulator. The project demonstrates the quantum algorithm’s ability to factor composite numbers efficiently, with a focus on **N = 15** and **N = 21**.

---

### **Key Features**
1. **Modular Exponentiation Oracle:**
   - Implements the core quantum oracle for modular exponentiation, a critical component of Shor’s algorithm.
   - Supports both **bottom-up** and **compiled** approaches for constructing the oracle circuit.

2. **Quantum Circuit Implementation:**
   - Builds the full quantum circuit for Shor’s algorithm, including:
     - Superposition of input states.
     - Modular exponentiation oracle.
     - Quantum Fourier Transform (QFT) for period finding.
   - Includes classical post-processing to extract factors from the period.

3. **Simulations:**
   - **N = 15:** Replicates the classic example, factoring 15 into 3 and 5.
   - **N = 21:** Extends the implementation to factor 21 into 3 and 7.

4. **Noise Analysis:**
   - Simulates realistic quantum noise using Qiskit’s noise models.
   - Compares the statistical error and success rates for N = 15 and N = 21 under noisy conditions.

5. **Performance Discussion:**
   - Analyzes the feasibility of scaling Shor’s algorithm to larger numbers on current quantum hardware.
   - Highlights challenges such as qubit requirements, circuit depth, and error rates.

---

### **Repository Structure**
```
project-7-shor/
│
├── src/
│   ├── shor_15.py          # Implementation for N=15
│   ├── shor_21.py          # Implementation for N=21
│   ├── modular_oracle.py   # Modular exponentiation oracle
│   └── noise_analysis.py   # Noise simulation and error analysis
│
├── notebook.ipynb          # visualization
├── README.md               # Project documentation
└── requirements.txt        # Dependencies (e.g., Qiskit)
```

---

### **Technologies Used**
- **Qiskit**: IBM’s quantum computing framework for circuit design and simulation.
- **Python**: Core programming language for implementation.
- **Jupyter Notebooks** (optional): For interactive exploration and visualization.

---

### **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/victor-pcll/Shor-s-factoring-algorithm
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### **Discussion**
- **Bottom-Up vs. Compiled Oracles:** Compares circuit depth and qubit requirements.
- **Noise Resilience:** Evaluates how statistical errors scale with problem size.
- **Future Work:** Potential optimizations and the path toward practical quantum factoring.

---

## References

[1] Stephane Beauregard. arXiv:quant-ph/0205095. Circuit for Shor’s algorithm using 2n+3 qubits, February 2003.

[2] Steven A. Cuccaro, Thomas G. Draper, Samuel A. Kutin, and David Petrie Moulton. A new quantum ripple-carry addition circuit, October 2004. arXiv:quant-ph/0410184.

[3] Thomas G. Draper. Addition on a Quantum Computer, August 2000. arXiv:quant-ph/0008033.

[4] Igor L. Markov and Mehdi Saeedi. Constant-Optimized Quantum Circuits for Modular Multiplication and Exponentiation, April 2015. arXiv:1202.6614 [cs].

[5] Omar Gamel and Daniel F. V. James. Simplified Factoring Algorithms for Validating Small-Scale Quantum Information Processing Technologies, November 2013. arXiv:1310.6446 [quant-ph].

[6] Robert L. Singleton Jr. Shor’s Factoring Algorithm and Modular Exponentiation Operators. Quanta, 12:41–130, September 2023. arXiv:2306.09122 [quant-ph].# Shor-s-factoring-algorithm




https://quantum.cloud.ibm.com/docs/en/guides

