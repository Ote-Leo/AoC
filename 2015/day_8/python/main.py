def parse_entry(arg):
    if arg[0] == '"':
        return parse_body(arg[1:], 0)

def parse_body(arg, counter):
    if len(arg) == 0 or arg[0] == '"':
        return counter
    
    skip = 1
    if arg[0] == '\\':
        skip = 2 if arg[1] == '"' or arg[1] == '\\' else 4
    
    return parse_body(arg[skip:], counter + 1)

def reencode(arg):
    res = 2
    for sym in arg:
        res += 2 if sym == '"' or sym == '\\' else 1
    return res

if __name__ == "__main__":

    with open('../input.txt') as file:
        part_i, part_ii = 0, 0

        for line in file:
            line = line.strip()
            part_i += len(line) - parse_entry(line)
            part_ii += reencode(line) - len(line)

        print('Part I')
        print('\tThe answer sholud be', part_i)
        print('Part II')
        print('\tThe answer should be', part_ii)


