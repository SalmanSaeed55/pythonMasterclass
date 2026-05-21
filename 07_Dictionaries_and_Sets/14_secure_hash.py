import hashlib

# print(*sorted(hashlib.algorithms_guaranteed), sep='\n')
# print()
# print(*sorted(hashlib.algorithms_available), sep='\n')

python_program = """for i in range(10:
print(i)"""
print(python_program)
print()

# for b in python_program.encode('utf-8'):
#     print(b, chr(b))

original_hash = hashlib.sha256(python_program.encode('utf-8'))
print(f"SHA256: {original_hash.hexdigest()}")

python_program += "print('code change')"
print(python_program)

new_hash = hashlib.sha256(python_program.encode('utf-8'))
print()
print(f"SHA256: {new_hash.hexdigest()}")