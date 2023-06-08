def is_nice(message: str) -> bool:
    vowel_count = 0
    contains_doubles = False
    contains_illegal = False

    illegal_list = ['ab', 'cd', 'pq', 'xy']

    itr = zip(message, message[1:] + '$')

    for (char, next) in itr:
        if char in 'aeiou': 
            vowel_count += 1
        if char == next:
            contains_doubles = True
        if (char + next) in illegal_list: 
            contains_illegal = True

    if vowel_count >= 3 and \
       contains_doubles and \
       not contains_illegal: 
        return True

    return False

def p2(message: str) -> bool:
    if p2r1(message) and p2r2(message):
        return True
    return False

def p2r1(message: str) -> bool: 
    for i in range(len(message) - 3):
        sub = message[i] + message[i + 1]
        for j in range(i + 2, len(message) - 1):
            new_sub = message[j] + message[j + 1]

            if sub == new_sub:
                return True
    return False

def p2r2(message: str) -> bool: 
    for i in range(len(message) - 2):
        if message[i] == message[i + 2]:
            return True

    return False



if __name__ == "__main__":
    with open('../input.txt') as file:
        nice_count = 0
        part_2 = 0

        for line in file:

            if is_nice(line):
                nice_count += 1

            if p2(line):
                part_2 += 1

        print('Part I')
        print(f'\tThere are {nice_count} nice strings!')

        print('Part II')
        print(f'\tThere are {part_2} nice strings!')
