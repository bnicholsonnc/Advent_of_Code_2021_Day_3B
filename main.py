#
# Benjamin Nicholson
# Advent of Code 2021
# Day 3 Part 2
#

def read_file(name):
    li = []
    file = open(name, 'r')
    for line in file:
        entry = line.rstrip()
        li.append(entry)
    file.close()
    return li


def main():
    o2_numbers = read_file('input.txt')
    co2_numbers = read_file('input.txt')

    try:
        for pos in range(len(o2_numbers[0])):
            if len(o2_numbers) == 1:
                break
            one = 0
            zero = 0
            for line in o2_numbers:
                if line[pos] == '1':
                    one += 1
                else:
                    zero += 1

            print(f'Ones: {one}')
            print(f'Zeros: {zero}')

            if one >= zero:
                keep = '1'
            else:
                keep = '0'

            o2_list = []

            for line in o2_numbers:
                if line[pos] == keep:
                    o2_list.append(line)

            o2_numbers = o2_list
            print(o2_numbers)

    except IndexError:
        pass

    try:

        for pos in range(len(co2_numbers[0])):
            if len(co2_numbers) == 1:
                break
            one = 0
            zero = 0
            for line in co2_numbers:
                if line[pos] == '1':
                    one += 1
                else:
                    zero += 1

            print(f'Ones: {one}')
            print(f'Zeros: {zero}')

            if one >= zero:
                keep = '0'
            else:
                keep = '1'

            co2_list = []

            for line in co2_numbers:
                if line[pos] == keep:
                    co2_list.append(line)

            co2_numbers = co2_list
            print(co2_numbers)

    except IndexError:
        pass

    print(f'Oxygen Generator Rating: {int(o2_list[0], 2)}')
    print(f'CO2 Scrubber Rating: {int(co2_list[0], 2)}')
    print(f'Life Support Rating: {int(o2_list[0], 2) * int(co2_list[0], 2)}')


main()
