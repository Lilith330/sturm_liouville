import numpy as np
from scipy.optimize import root_scalar
from scipy.special import j0, j1

def bessel_root_finder(alpha, R, num_roots=4):
    roots = []
    search_start = 1e-5
    step = np.pi / R
    
    while len(roots) < num_roots:
        try:
            sol = root_scalar(lambda l: j0(l * R) + alpha * l * j1(l * R),
                              bracket=[search_start, search_start + step],
                              method='brentq')
            if sol.converged:
                roots.append(sol.root)
                search_start = sol.root + step / 2 
        except ValueError:
            search_start += step
    
    return roots
alpha = float(input("Enter \u03b1: "))
R = float(input("Enter R: "))
lambdas = bessel_root_finder(alpha, R)
print("First 4 lambdas:", lambdas)
