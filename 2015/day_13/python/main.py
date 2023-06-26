from typing import TypeVar

X = TypeVar('X')


def parse_line(line: str, ctx: dict[tuple[str, str], int], people: list[str]) -> None:
    tokens = line.split(' ')
    p1, p2 = tokens[0][0], tokens[-1][0]
    key = (p1, p2) if p1 < p2 else (p2, p1)
    val = int(tokens[3]) * (-1 if tokens[2] == 'lose' else 1)
    val += ctx.get(key, 0)
    ctx[key] = val
    if p1 not in people:
        people.append(p1)

def permute(lst: list[X]) -> list[list[X]]:
    if not lst:
        return []
    elif len(lst) == 1:
        return [lst]
    elif len(lst) == 2:
        return [[lst[0], lst[1]], [lst[1], lst[0]]]
    
    res: list[list[X]] = []

    for i in range(len(lst)):
        head = lst[i]
        perms = permute(lst[:i] + lst[i+1:])
        res += [[head] + perm for perm in perms]
    
    return res
    
def get_cost(a: str, b: str, ctx: dict[tuple[str, str], int]) -> int:
    if (a,b) in ctx.keys():
        return ctx[(a,b)]
    return ctx[(b,a)]
    
def calc_cost(lst: list[str], ctx: dict[tuple[str, str], int]) -> int:
    res = 0
    for i in range(len(lst) - 1):
        res += get_cost(lst[i], lst[i + 1], ctx)
    res += get_cost(lst[0], lst[-1], ctx)
    return res

def ultimate_seating(people: list[str], ctx: dict[tuple[str, str], int]) -> int:
    return max(map(lambda s: calc_cost(s, ctx), permute(people)))

if __name__ == '__main__':
    with open('../input.txt') as file:
        ctx = {}
        people: list[str] = []
        for line in file:
            parse_line(line, ctx, people)
        print(f'Part I')
        print(f'\tUltimate seating value is {ultimate_seating(people, ctx)}')
        ctx: dict[tuple[str, str], int] = ctx | {(p, 'Z'): 0 for p in people}
        people.append('Z')
        print(f'Part II')
        print(f'\tUltimate seating value is {ultimate_seating(people, ctx)}')