import json

def calculate_kendall_tau(rank_a, rank_b):
    pairs = combinations(range(1, len(rank_a) + 1), 2)
    discordant_pairs = 0
    for x, y in pairs:
        a = rank_a.index(x) - rank_a.index(y)
        b = rank_b.index(x) - rank_b.index(y)
        if a * b < 0:
            discordant_pairs += 1
    total_pairs = len(rank_a) * (len(rank_a) - 1) / 2
    coefficient = 1 - 2 * discordant_pairs / total_pairs
    return round(coefficient, 2)


def consensus_ranking(json_a, json_b):

    rank_a = json.loads(json_a)
    rank_b = json.loads(json_b)

    all_items = set()
    [all_items.update(item if isinstance(item, list) else [item]) for item in rank_a]
    [all_items.update(item if isinstance(item, list) else [item]) for item in rank_b]

    clusters = []
    for item in all_items:
        found_cluster = False
        for cluster in clusters:
            if item in cluster:
                found_cluster = True
                break
        if not found_cluster:

            new_cluster = set()

            [new_cluster.update(neighbor if isinstance(neighbor, list) else [neighbor])
             for neighbor in rank_a if item in (neighbor if isinstance(neighbor, list) else [neighbor])]
            [new_cluster.update(neighbor if isinstance(neighbor, list) else [neighbor])
             for neighbor in rank_b if item in (neighbor if isinstance(neighbor, list) else [neighbor])]
            clusters.append(new_cluster)

    merged = True
    while merged:
        merged = False
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                if clusters[i].intersection(clusters[j]):
                    clusters[i].update(clusters[j])
                    del clusters[j]
                    merged = True
                    break
            if merged:
                break

    clusters = [list(cluster) for cluster in clusters]

    clusters = [sorted(cluster) for cluster in clusters]
    clusters.sort(key=lambda x: (len(x), x))

    return json.dumps(clusters)


# Примеры ранжировок
json_a = json.dumps([1,[2,3],4,[5,6,7],8,9,10])
json_b = json.dumps([[1,2],[3,4,5,],6,7,9,[8,10]])
json_c = json.dumps([3,[1,4],2,6,[5,7,8],[9,10]])

# Получение согласованной кластерной ранжировки
result = consensus_ranking(json_a, json_c)
print(result)
