def calc_floor(steps: str,  basement_instance = 0) -> tuple[int, int]:
    floor = 0
    in_basement = False

    for (idx, step) in enumerate(steps):
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1

        if floor == -1 and (not in_basement): 
            in_basement = True
            basement_step = idx + 1

    return (basement_step, floor)

if __name__ == "__main__":
    with open('../input.txt') as f:
        (in_basement, floor) = calc_floor(f.readline())
        print(f'Santa Should be on floor: {floor}; He entered the floor at step: {in_basement}')

