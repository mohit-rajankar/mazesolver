# bayesian.py
def bayesian_update(prior, reading, accuracy=0.8):
    likelihood = accuracy if reading == 1 else (1 - accuracy)

    posterior = (likelihood * prior) / (
        likelihood * prior + (1 - likelihood) * (1 - prior)
    )

    return posterior
