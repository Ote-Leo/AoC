def uint16(num): 
    return num & 0xFFFF

def parse_command(idx, command, registers):
    tokens = command.split(' ')
    register = tokens[-1]
    instruction = tokens[:-2]
    instruction_length = len(instruction)

    if instruction_length == 1:
        input = instruction[0]
        registers[register] = uint16(int(input)) if not input.isalpha() else input

    elif instruction_length == 2:
        if instruction[0] == 'NOT':
            registers[register] = ('NOT', instruction[1])
            
    else:
        x = instruction[0]
        y = instruction[2]
        opcode = instruction[1]

        if opcode == 'LSHIFT' or opcode == 'RSHIFT':
            registers[register] = (opcode, x, uint16(int(y)))
        else:
            x = uint16(int(x)) if x.isdecimal() else x
            registers[register] = (opcode, x, y)

def eval_register(register, registers):
    register_val = registers[register]

    if type(register_val) == int: return register_val

    if type(register_val) != tuple:
        registers[register] = eval_register(register_val, registers)
        return registers[register]

    instruction = register_val[0]
    x = register_val[1]

    if instruction == 'NOT':
        registers[register] = uint16(~x) if type(x) == int else uint16(~eval_register(x, registers))
        return registers[register]

    y = register_val[2]
    if instruction == 'LSHIFT' or instruction == 'RSHIFT':
        dep_val = eval_register(x, registers)
        registers[register] = uint16(dep_val << y) if instruction == 'LSHIFT' else uint16(dep_val >> y)
        return registers[register]

    x = x if type(x) == int else eval_register(x, registers)
    y = y if type(y) == int else eval_register(y, registers)
    registers[register] = uint16(x & y) if instruction == 'AND' else uint16(x | y)
    return registers[register]



if __name__ == "__main__":
    with open('../input.txt') as file:
        registers_1: dict[str, str|int] = {}
        for idx, line in enumerate(file):
            parse_command(idx, line.strip(), registers_1)

        registers_2 = registers_1.copy()
        a_val = eval_register('a', registers_1)
        registers_2['b'] = a_val
        b_val = eval_register('a', registers_2)

        print('Part I')
        print(f"\tThe value of `a' should be {a_val}")
        print('Part II')
        print(f"\tThe value of `a' should be {b_val}")
