import bayes

def test_basic_compute_posterior():
    """
    This checks that the computation

    P(A | B) = P(B | A) P(A) / P(B)

    is correct for

    P(B | A) = 1 / 3
    P(A) = 1 / 4
    P(B) = 1 / 8

    which in our case gives:

    P(A | B) = 2 / 3

    """
    conditional = 1 / 3
    prior = 1 / 4
    marginal = 1 / 8
    posterior = bayes.compute_posterior(marginal=marginal, prior=prior, conditional=conditional)
    expected_posterior = 2 / 3
    assert posterior == expected_posterior, f"Posterior obtained was {posterior}"


def test_another_compute_posterior_values():
    """
    This is a similar test to `test_basic_compute_posterior` but with different values.
    
    This is in fact the same test that is in the documentation.
    """
    conditional = .1
    prior = 0.2
    marginal = 0.05
    posterior = round(bayes.compute_posterior(marginal=marginal, prior=prior, conditional=conditional), 1)
    expected_posterior = .4
    assert posterior == expected_posterior, f"Posterior obtained was {posterior}"

test_basic_compute_posterior()
test_another_compute_posterior_values()