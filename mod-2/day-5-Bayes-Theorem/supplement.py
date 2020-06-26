def create_dist(sample, parameters=[5, 1]):
    mu = parameters[0]
    sigma = parameters[1]

    X = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)

    plt.plot(X, norm.pdf(X, loc=mu, scale=sigma))

    plt.scatter(sample, norm.pdf(sample, loc=mu, scale=sigma), color='r')

    plt.show()
    
with open('sample.pickle', 'rb') as handle:
    s = pickle.load(handle)


def is_drug(sensitivity, specificity, prior):
    likelihood = sensitivity

    denom = prior * sensitivity + (1 - prior) * (1 - specificity)

    return likelihood * prior / denom


import random
def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print("P(both | older):", both_girls / older_girl )     # 0.514 ~ 1/2
print("P(both | either): ", both_girls / either_girl)   # 0.342 ~ 1/3