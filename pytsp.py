def nearthest_insertion_algorithm(graph):
    if graph.size == 0:
        return -1, []

    points = range(graph.size())

    current = points[0]

    points.remove(current)

    i = current
    j = points[0]
    cij = graph.get_distance(i, j)
    for point in points:
        if graph.get_distance(i, point) < cij:
            cij = graph.get_distance(i, point)
            j = point

    points.remove(j)

    edges = [(i, j)]

    visited = []
    visited.append(i)
    visited.append(j)

    while len(points) > 0:
        i = visited[0]
        k = points[0]
        crj = graph.get_distance(k, i)

        for point in points:
            for c in visited:
                dist = graph.get_distance(point, c)
                if dist < crj:
                    k = point

        i = edges[0][0]
        j = edges[0][1]
        c_min = graph.get_distance(i, k) + graph.get_distance(k, j) - graph.get_distance(i, j)

        for e in edges:
            aux_i = e[0]
            aux_j = e[1]
            dist = graph.get_distance(aux_i, k) + graph.get_distance(k, aux_j) - graph.get_distance(aux_i, aux_j)
            if dist < c_min:
                c_min = dist
                i = aux_i
                j = aux_j

        edges.remove((i, j))
        edges.append((i, k))
        edges.append((k, j))

        visited.append(k)
        points.remove(k)

    cost = 0
    for e in edges:
        i = e[0]
        j = e[1]
        cost += graph.get_distance(i, j)

    return cost, edges