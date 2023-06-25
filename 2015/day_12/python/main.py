import json
from typing import Any

def p_num(msg: str, i: int, factor: int = 1) -> tuple[int, int]:
    num = ''

    while i < len(msg):
        if msg[i].isdigit():
            num += msg[i]
            i += 1
        else:
            return (factor * int(num), i)

    return (0, i)


def sum_nums(msg: str) -> int:
    res = 0

    i = 0
    while i < len(msg):
        dr = 0
        if msg[i] == '-':
            (dr, i) = p_num(msg, i + 1, -1)
        elif msg[i].isdigit():
            (dr, i) = p_num(msg, i)
        else:
            i += 1

        res += dr

    return res

def sum_no_red(obj: int | list[Any] | dict[Any, Any]) -> int:
    "We're going full JSON parsing for simplicity sake"
    if type(obj) == int:
        return obj
    if type(obj) == list:
        return sum([sum_no_red(item) for item in obj])
    if type(obj) == dict:
        if "red" in obj.values():
            return 0
        return sum_no_red(list(obj.values()))
    return 0

if __name__ == '__main__':
    with open('../input.json') as file:
        for line in file:
            part_i = sum_nums(line)
            print(f'Part I')
            print(f'\tThe answer should be {part_i}')
    
            part_ii = sum_no_red(json.loads(line))
            print('Part II')
            print(f'\tThe answer should be {part_ii}')
            