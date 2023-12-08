from statistics import mean

from distances import (
    dist_euclidean,
    ngram_jaccard_distance,
)

def simple_tokenizer(s):
    return s.split()

def mean_dist(embeddings, distance=dist_euclidean):
    """
    computes mean distance from all samples to the centroid

    this is sample variance when euclidean distance is used
    """
    (n, d) = embeddings.shape
    centroid = embeddings.mean(0)
    distances = []
    for i in range(n):
        distances.append(distance(centroid, embeddings[i]))
    return mean(distances)

def diversity_text(
        data,
        datatype="token",
        distance_function=ngram_jaccard_distance,
        tokenizer=simple_tokenizer,
    ):
    assert datatype in ["token", "character"]
    if datatype == "token":
        X = [tokenizer(s) for s in data]
    elif datatype == "character":
        X = data
    tally = 0
    for a in X:
        for b in X:
            d = distance_function(a, b)
                tally += d
    score = tally / (len(X) ** 2)
    return score
