# sturm_liouville
The code receives alpha, beta and L parameters in the input and returns the first 4 lambdas as a result


    The Sturm-Liouville problem

    y'' + (lambda^2)y = 0
    y(0) = alpha * y'(0)
    y(L) = beta * y'(L)

    Parameters:
    alpha: float - Boundary condition at x=0: y(0) = alpha * y'(0).
    beta:  float - Boundary condition at x=L: y(L) = beta * y'(L).
    L:     float - Length of the domain.
    num_eigenvalues: int - Number of eigenvalues to compute. In the code it is equal to 4.

    Returns:
    lambdas: ndarray - Computed eigenvalues (lambda).
