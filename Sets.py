#Sets
L = [1,2,3,4,5,5]
new = set(L)
print(new)

L = [1,2,3,4,5,5]
print(len(L))

a = {1,2,3,4,5,}
a.add("India")
print(a)

a = {1,2,3,4,5, 'India'}
a.remove('India')
print(a)

grades = ['A','B','C','D','A','B','C','D']
new = set(grades)
print(new)

# Set Operations
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print(A|B)
print(A.union(B))

A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print(A & B)
print(A.intersection(B))

A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print(A - B)
print(A.difference(B))











