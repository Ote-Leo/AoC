
from hashlib import md5

SAMPLE_INPUT = [
    ('abcdef', 609043),
    ('pqrstuv', 1048970),
]

def check_hex(hex: str, n: int) -> bool:
    for i in range(n):
        if hex[i] != '0':
            return False

    return True

if __name__ == "__main__":

    key = 'iwrupvqb'

    with open('../input.txt') as file:
        for line in file:
            key = line

            num = 0
            hasher = md5()
            hasher.update(bytes(key, 'utf8'))

            while True:
                hashx = hasher.copy()
                hashx.update(bytes(str(num), 'utf8'))
                hash = hashx.hexdigest()

                if check_hex(hash, 5): break

                num += 1

            print('Part I')
            print(f'\tKey:\t{key}\tNumber:\t{num}')
            print(f'\thash:\t{hash}')


            num = 0
            while True:
                hashx = hasher.copy()
                hashx.update(bytes(str(num), 'utf8'))
                hash = hashx.hexdigest()

                if check_hex(hash, 6): break

                num += 1


            print('\nPart II')
            print(f'\tKey:\t{key}\tNumber:\t{num}')
            print(f'\thash:\t{hash}')
