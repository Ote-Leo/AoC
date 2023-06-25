from typing import Iterator

FORB_NUMS = [ord('i'), ord('o'), ord('l')]

def show_password(password: list[int]) -> str:
    return ''.join(map(chr, reversed(password)))

def parse_input(line: str) -> list[int]:
    r: list[int] = []
    for c in reversed(line):
        r.append(ord(c))
    return r

def rule_1(msg: list[int]) -> bool:
    for i in range(len(msg) - 2):
        if msg[i] == msg[i + 1] + 1 and msg[i + 1] == msg[i + 2] + 1:
            return True
    return False

def rule_2(msg: list[int]) -> bool:
    for c in msg:
        if c in FORB_NUMS:
            return False
    return True

def rule_3(msg: list[int]) -> bool:
    pair_count = 0
    fpair_head = ''

    for i in range(len(msg) - 1):
        if msg[i] == fpair_head:
            continue
        elif msg[i] == msg[i + 1]:
            pair_count += 1
            fpair_head = msg[i]

    return False if pair_count < 2 else True

def safe_inc(msg: list[int]) -> list[int]:
    r = msg

    for i in range(len(r)):
        r[i] += 1
        if r[i] > ord('z'):
            r[i] = ord('a')
        else:
            break

    return r

def passwords(msg: list[int]) -> Iterator[list[int]]:
    while True:
        msg = safe_inc(msg)
        yield msg

def next_password(msg: list[int]) -> Iterator[str]:
    for password in passwords(msg):
        if rule_1(password) and rule_2(password) and rule_3(password):
            yield show_password(password)



if __name__ == '__main__':
    with open('../input.txt') as file:
        for line in file:
            valid_pass = next_password(parse_input(line))
            for i in range(2):
                print(f'Part {i + 1}')
                print(f'\tThe next password should be {next(valid_pass)}')