import sys

stairs_amount = int(sys.argv[1])
for i in range(1, stairs_amount + 1):
    print(' ' * (stairs_amount - i), '#' * i, sep='')