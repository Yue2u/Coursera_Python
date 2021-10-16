import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D_root_ = float(math.sqrt(b * b - 4 * a * c))
print(int(((-b + D_root_) / (2 * a))))
print(int(((-b - D_root_) / (2 * a))))
