import numpy as np
## with chat-gpt


def privacy_aggregation(teacher_epsilons):
    """
    Calculates the privacy loss of an ensemble of teachers by aggregating their privacy budgets using the advanced composition theorem.
    Args:
    teacher_epsilons (list of float): list of privacy budgets of the teachers in the ensemble
    Returns:
    float: aggregate privacy loss
    """
    k = len(teacher_epsilons)
    epsilons_squared = [e**2 for e in teacher_epsilons]
    epsilon_star = np.sqrt(np.sum(epsilons_squared))
    delta_star = 1/k
    return epsilon_star, delta_star
