def handle_input(input: str,
                 init_pos: tuple[int, int],
                 houses: dict[tuple[int, int], int]) -> ():
    pos = list(init_pos)

    for direction in input:
        
        if direction == '^':   pos[1] += 1
        elif direction == '>': pos[0] += 1
        elif direction == 'v': pos[1] -= 1
        elif direction == '<': pos[0] -= 1

        idx = tuple(pos)
        houses.setdefault(idx, 0)
        houses[idx] += 1


if __name__ == "__main__":
    houses: dict[tuple[int, int], int] = {}

    init_pos = (0, 0)
    houses[init_pos] = 1

    with open('../input.txt') as file:
        for line in file:
            handle_input(line, init_pos, houses)
            output = len(houses.items())

            print(f'Santa has visited {output} houses')

            houses = {}
            houses[init_pos] = 1

            handle_input(line[::2], init_pos, houses)
            handle_input(line[1::2], init_pos, houses)
            print(f'Santa & Robo-Santa have visited: {len(houses.items())} houses')


