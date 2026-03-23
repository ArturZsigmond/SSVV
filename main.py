def read_sequence(n):
    arr = []
    for i in range(n):
        try:
            val = int(input())
        except:
            print("Invalid input detected")
            exit(1)
        arr.append(val)
    return arr

def compute_a_sequence(start, n, arr):
    distinct = set()
    length = 0

    for i in range(start, n):
        if arr[i] not in distinct and len(distinct) == 3:
            break

        distinct.add(arr[i])
        length += 1

    return length


def compute_max_seq(n, arr):
    max_len = 0
    start = 0

    for i in range(n):
        length = compute_a_sequence(i, n, arr)

        if length > max_len:
            max_len = length
            start = i

    return start, max_len


def print_sequence(arr, start, length):
    print("Start:", start)
    print("Length:", length)

    for i in range(start, start + length):
        print(arr[i], end=" ")
    print()


def main():
    try:
        n = int(input())
    except:
        print("Invalid input for n")
        return

    if n <= 0:
        print("n must be >= 1")
        return

    arr = read_sequence(n)

    start, length = compute_max_seq(n, arr)

    print_sequence(arr, start, length)


if __name__ == "__main__":
    main()
