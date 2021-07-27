import ctypes
import sys


def ref_count(address):
    return ctypes.c_long.from_address(address).value


my_var = [1, 2, 3]

#coutn is 1
print(ref_count(id(my_var)))

# count is 2 because called method take my_var as an argument(receives and stores a reference to my_var)
print(sys.getrefcount(my_var))

other_var = my_var

# count is 2 now
print(ref_count(id(my_var)))

other_var = None

# count is 1 again
print(ref_count(id(my_var)))
