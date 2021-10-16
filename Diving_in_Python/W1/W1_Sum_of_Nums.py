import sys

if __name__ == "__main__":
    _sum = 0
    for num in sys.argv[1]:
        _sum += int(num)
    print(_sum)
