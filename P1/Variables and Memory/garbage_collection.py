import ctypes
import gc


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists in GC!"

    return "Object not found in GC."


class A:
    def __init__(self):
        self.b = B(self)
        print(f"A: self: {id(self)}, b: {id(self.b)}")


class B:
    def __init__(self, a):
        self.a = a
        print(f"B: self: {id(self)}, a: {id(self.a)}")


# To see the memory leak
gc.disable()

my_var = A()

a_id = id(my_var)
b_id = id(my_var.b)

# 2, 1 and Object Exists
print(f"refcount A: {ref_count(a_id)}")
print(f"refcount B: {ref_count(b_id)}")
print(f"A: {object_by_id(a_id)}")
print(f"B: {object_by_id(b_id)}")

# Delete the object reference
my_var = None

# 1, 1 and Object Exists which lead to memory leak as those aren't used anywhere in the code
print(f"refcount A: {ref_count(a_id)}")
print(f"refcount B: {ref_count(b_id)}")
print(f"A: {object_by_id(a_id)}")
print(f"B: {object_by_id(b_id)}")

# Leave memory management to GC's hand
gc.collect()

# All are taken care of. :)
print(f"refcount A: {ref_count(a_id)}")
print(f"refcount B: {ref_count(b_id)}")
print(f"A: {object_by_id(a_id)}")
print(f"B: {object_by_id(b_id)}")
