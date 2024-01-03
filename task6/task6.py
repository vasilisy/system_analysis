import json
from itertools import combinations


def flatten_ranking(ranking):
    flat_rank = []
    for elem in ranking:
        if isinstance(elem, list):
            flat_rank.extend(elem)
        else:
            flat_rank.append(elem)
    return flat_rank


def calculate_kendall_tau(rank_a, rank_b):
    pairs = combinations(range(1, len(rank_a) + 1), 2)
    discordant_pairs = 0
    for x, y in pairs:
        a_x, a_y = rank_a.index(x), rank_a.index(y)
        b_x, b_y = rank_b.index(x), rank_b.index(y)
        if (a_x - a_y) * (b_x - b_y) < 0:
            discordant_pairs += 1
    total_pairs = len(rank_a) * (len(rank_a) - 1) / 2
    coefficient = 1 - 2 * discordant_pairs / total_pairs
    return round(coefficient, 2)


def task(rank_a_json, rank_b_json, rank_c_json):
    rank_a = json.loads(rank_a_json)
    rank_b = json.loads(rank_b_json)
    rank_c = json.loads(rank_c_json)

    flat_rank_a = flatten_ranking(rank_a)
    flat_rank_b = flatten_ranking(rank_b)
    flat_rank_c = flatten_ranking(rank_c)

    kendall_ab = calculate_kendall_tau(flat_rank_a, flat_rank_b)
    kendall_ac = calculate_kendall_tau(flat_rank_a, flat_rank_c)

    print(f"A and B: {kendall_ab}")
    print(f"A and C: {kendall_ac}")


rank_a_json = "[1,[2,3],4,[5,6,7],8,9,10]"
rank_b_json = "[[1,2],[3,4,5],6,7,9,[8,10]]"
rank_c_json = "[3,[1,4],2,6,[5,7,8],[9,10]]"
task(rank_a_json, rank_b_json, rank_c_json)
