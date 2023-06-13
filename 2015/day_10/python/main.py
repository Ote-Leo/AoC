from typing import Sequence


def group(lst: Sequence) -> Sequence[Sequence]:
    groups = []
    sub_group = []
    elem = None

    for x in lst:
        if not elem:
            elem = x
            sub_group = [elem]
        elif x == elem:
            sub_group.append(x)
        else:
            elem = x
            groups.append(sub_group)
            sub_group = [elem]
    if sub_group:
        groups.append(sub_group)

    return groups


def count_and_say(line: str) -> str:
    groups = group(line)
    res = ''
    for gpx in groups:
        res += str(len(gpx)) + gpx[0]
    return res


if __name__ == '__main__':
    with open('../input.txt') as file:
        for line in file:
            bfx = line.strip()

            msg = ''
            for i in range(40):
                msg = count_and_say(bfx)
                bfx = msg

            part_i = len(msg)

            for i in range(10):
                msg = count_and_say(bfx)
                bfx = msg

            part_ii = len(msg)

            print('Part I')
            print(f'\tThe answer should be {part_i}')
            print('Part I')
            print(f'\tThe answer should be {part_ii}')
