import numpy as np
from numpy.random import laplace

## co-author with chat-gpt style.

def l1_dp(array1, array2):
    """
    Calculates the differential privacy between two numpy arrays using L1 sensitivity measure
    Args:
    array1 (numpy array): first array
    array2 (numpy array): second array
    Returns:
    float: differential privacy
    """
    sensitivity = np.linalg.norm(array1 - array2, ord=1)
    epsilon = 1.0
    differential_privacy = sensitivity / epsilon
    return differential_privacy


def laplace_l1_dp(array1, array2, epsilon):
    """
    Calculates the differential privacy between two numpy arrays using L1 sensitivity measure
    and adding Laplace noise to the result.
    Args:
    array1 (numpy array): first array
    array2 (numpy array): second array
    epsilon (float): privacy budget
    Returns:
    float: differential privacy
    """
    sensitivity = np.linalg.norm(array1 - array2, ord=1)
    scale = sensitivity / epsilon
    differential_privacy = laplace(scale=scale)
    return differential_privacy
