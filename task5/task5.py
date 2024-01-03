import json


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

# Получение согласованной кластерной ранжировки
result = consensus_ranking(json_a, json_b)
print(result)
