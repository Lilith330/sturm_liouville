import numpy as np
from scipy.optimize import root_scalar

def solve_sturm_liouville(alpha, beta, L, num_eigenvalues=4):
    def boundary_condition_equation(lmbda):
        if lmbda == 0:
            return np.inf 
        term1 = (alpha * lmbda - beta * lmbda) * np.cos(lmbda * L)
        term2 = (1 + beta * alpha * lmbda**2) * np.sin(lmbda * L)
        return term1 + term2
      
    guesses = [(n * np.pi) / L for n in range(1, num_eigenvalues + 1)]
    lambdas = []
    for guess in guesses:
        result = root_scalar(
            boundary_condition_equation,
            bracket=[guess - np.pi / (2 * L), guess + np.pi / (2 * L)],
            method='brentq'
        )
        if result.converged:
            lambdas.append(result.root)
    return np.array(lambdas)
  
alpha = float(input("Enter boundary condition \u03b1 (at x=0): "))
beta = float(input("Enter boundary condition \u03b2 (at x=L): "))
L = float(input("Enter domain length L: "))

num_eigenvalues = 4
lambdas = solve_sturm_liouville(alpha, beta, L, num_eigenvalues)

print("Computed eigenvalues (lambda):")
for i, lmbda in enumerate(lambdas, start=1):
    lambdas_in_pi = lmbda / np.pi
    print(f"\u03bb[{i}] = {lmbda:.5f} = {lambdas_in_pi:.5f} * π")
