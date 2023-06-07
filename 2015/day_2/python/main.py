if __name__ == "__main__":

    with open('../input.txt') as file:
        total_area = 0
        total_ribbons = 0

        for line in file:
            dim = list(map(int, line.split('x')))
            dim.sort()
            a1, a2, a3 = dim[0] * dim[1], dim[0] * dim[2], dim[1] * dim[2]
            total_area += a1 + 2 * (a1 + a2 + a3)

            prod = a1 * dim[2]

            perimeter = 2 * (dim[0] + dim[1])
            total_ribbons += perimeter + prod


        print(f'Total area required is: {total_area}; With ribbons of {total_ribbons} feet.')
