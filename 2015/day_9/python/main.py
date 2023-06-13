def permute(lst: list) -> list[list]:
    if len(lst) == 0:
        return lst
    if len(lst) == 1:
        return [lst]

    res: list[list] = []
    for i in range(len(lst)):
        lst_rem = lst[:i] + lst[i + 1:]
        for perm in permute(lst_rem):
            res.append([lst[i]] + perm)

    return res


def route_distance(graph: list[list[int]], route: list[int]) -> int:
    distance = 0
    for (x, y) in zip(route, route[1:]):
        distance += graph[x][y]
    return distance


if __name__ == "__main__":
    with open('../input.txt') as file:
        countries_idx = []
        distances = []

        for line in file:
            parts = line.strip().split(' ')
            country_a, country_b, distance = parts[0], parts[2], int(parts[-1])

            if country_a not in countries_idx:
                countries_idx.append(country_a)
            if country_b not in countries_idx:
                countries_idx.append(country_b)

            distances.append((countries_idx.index(country_a),
                              countries_idx.index(country_b),
                              int(distance)))

        graph = [[0] * len(countries_idx) for _ in range(len(countries_idx))]
        for ptx in distances:
            graph[ptx[0]][ptx[1]] = ptx[2]
            graph[ptx[1]][ptx[0]] = ptx[2]

        countries = [x for x in range(len(countries_idx))]
        routes = permute(countries)
        min_distance, max_distance = route_distance(
            graph, routes[0]), route_distance(graph, routes[0])
        for route in routes[1:]:
            current_distance = route_distance(graph, route)
            if current_distance < min_distance:
                min_distance = current_distance
            elif current_distance > max_distance:
                max_distance = current_distance

        print('Part I')
        print(f'\tThe minimum distance should be {min_distance}')
        print('Part II')
        print(f'\tThe maximum distance should be {max_distance}')
