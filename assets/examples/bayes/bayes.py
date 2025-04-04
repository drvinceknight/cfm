def compute_posterior(conditional, prior, marginal):
    """
    This computes the posterior probability as given by Bayes' theorem.

    Bayes' theorem is:

    P(A | B) P(B) = P(B | A) P(A)

    Where:

    - P(A) is the prior
    - P(B) is the marginal
    - P(B | A) is the conditional

    and P(A | B) is the posterior

        Parameters
    ----------
    conditional : float
        the conditional probability, must be between 0 and 1
    marginal : float
        the marginal probability, must be between 0 and 1
    prior : float
        the prior probability, must be between 0 and 1

    Returns
    -------
    float
        the posterior probability
    """
    return conditional * prior / marginal