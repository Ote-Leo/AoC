import time

def exe_inst(inst: str, grid: list[list[int]]):
    inst_parts = inst.split(' ')
    inst = inst_parts[0]
    start_pnt = tuple(map(int, inst_parts[-3].split(',')))
    end_pnt = tuple(map(int, inst_parts[-1].split(',')))

    for i in range(start_pnt[0], end_pnt[0] + 1):
        for j in range(start_pnt[1], end_pnt[1] + 1):
            if inst == 'toggle':
                grid[i][j] = 0 if grid[i][j] == 1 else 1
            elif inst_parts[1] == 'on':
                grid[i][j] = 1
            else:                                 
                grid[i][j] = 0

def part_two(inst: str, grid: list[list[int]]):
    inst_parts = inst.split(' ')
    inst = inst_parts[0]
    start_pnt = tuple(map(int, inst_parts[-3].split(',')))
    end_pnt = tuple(map(int, inst_parts[-1].split(',')))

    for i in range(start_pnt[0], end_pnt[0] + 1):
        for j in range(start_pnt[1], end_pnt[1] + 1):
            if inst == 'toggle':
                grid[i][j] += 2
            elif inst_parts[1] == 'on':
                grid[i][j] += 1
            else:
                grid[i][j] = max(grid[i][j] - 1, 0)
    

if __name__ == '__main__':

    start_time = time.time()

    lit_points = 0
    grid = [[0] * 1000 for _ in range(1000)]

    with open('../input.txt') as file:
        for line in file: 
            exe_inst(line, grid)

        lit_points = sum(sum(row) for row in grid)
        print('Part I')
        print(f'\tThere should be {lit_points} lit points.')

    lit_points = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] = 0

    with open('../input.txt') as file:
        for line in file:
            part_two(line, grid)

        lit_points = sum(sum(row) for row in grid)

        print('Part II')
        print(f'\tThe over all intensity should be {lit_points}.')


    end_time = time.time()

    print(f'Execution took {end_time - start_time}')

