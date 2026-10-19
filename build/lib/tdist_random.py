"""Generate random numbers from a Student's t-distribution
with a given mean, variance and degrees of freedom."""

import math
import random

__all__ = ["t_random"]


def t_random(mean, variance, df, n, seed=None):
    """Return a list of `n` samples from a location-scale t-distribution.

    mean     -- mean of the distribution
    variance -- variance of the distribution (the real variance, not the scale^2)
    df       -- degrees of freedom (t value parameter); must be > 2
                so that the variance is finite
    n        -- number of samples to return
    seed     -- optional seed for reproducibility
    """
    if df <= 2:
        raise ValueError("df must be > 2 (variance is infinite otherwise)")
    if variance < 0:
        raise ValueError("variance must be >= 0")
    if n < 0:
        raise ValueError("n must be >= 0")

    rng = random.Random(seed)
    # Var[scale * T_df] = scale^2 * df / (df - 2)
    scale = math.sqrt(variance * (df - 2) / df)
    out = []
    for _ in range(int(n)):
        z = rng.gauss(0.0, 1.0)
        chi2 = rng.gammavariate(df / 2.0, 2.0)
        out.append(mean + scale * z / math.sqrt(chi2 / df))
    return out
