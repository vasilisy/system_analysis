def task(graph):

    res = [set() for _ in range(5)]
    lst = []

    all_keys = []
    for key in graph:

        if key not in all_keys:
            all_keys.append(key)


        for elem in graph[key]:
            if elem not in all_keys:
                all_keys.append(elem)


    for key in graph:
        for elem in graph[key]:
            node1 = int(key)
            node2 = int(elem)
            lst.append((node1, node2))
            res[0].add(node1)
            res[1].add(node2)


    for edge in lst:
        node1, node2 = edge


        for edge_inner in lst:
            if node2 == edge_inner[0]:
                res[2].add(node1)
                res[3].add(edge_inner[1])


        if list(zip(*lst))[0].count(node1) > 1:
            res[4].add(node2)


    res = [sorted(list(s)) for s in res]
    inner_strings = [",".join(str(num) for num in el) for el in res]
    stree = "\n".join(inner_strings)
    return stree




graph = {'1': ['2', '3'], '3': ['4', '5'], '4': ['6']}
print(task(graph))
