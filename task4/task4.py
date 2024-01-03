import numpy as np


def combined_task():
    table = np.zeros((13, 37))
    for i in range(1, 7):
        for j in range(1, 7):
            table[i + j][i * j] += 1


    probs = table / 36

    Hab = -np.sum(probs * np.log2(probs, where=(probs != 0)))

    A_probs = np.sum(probs, axis=1)
    B_probs = np.sum(probs, axis=0)

    Ha = -np.sum(A_probs * np.log2(A_probs, where=(A_probs != 0)))
    Hb = -np.sum(B_probs * np.log2(B_probs, where=(B_probs != 0)))

    HaB = Hab - Ha

    Iab = Hb - HaB

    print(f"H(AB) = {Hab:.2f}")
    print(f"H(A) = {Ha:.2f}")
    print(f"H(B) = {Hb:.2f}")
    print(f"Ha(B) = {HaB:.2f}")
    print(f"I(A,B) = {Iab:.2f}")

    return [round(Hab, 2), round(Ha, 2), round(Hb, 2), round(HaB, 2), round(Iab, 2)]


combined_results = combined_task()
