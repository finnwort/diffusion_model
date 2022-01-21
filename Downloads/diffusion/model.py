def energy(density, coeff=1.0):
    return sum([x*(x-1) for x in density if x > 0])
    """Energy associated with the diffusion model

    Parameters
    ----------

    density: array of positive integers
        Number of particles at each position i in the array
    coeff: float
        Diffusion coefficient.
    """
    # implementation goes here
