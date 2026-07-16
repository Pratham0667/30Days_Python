A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(f" JOIN OPP  : {A.union(B)}")

print(f"THE INTERSECTION : {A.intersection(B)}")

print(f"IS A IS SUBSET OF B  : {A.issubset(B)}")

print(f" ARE A DISJOINT SET  : {A.isdisjoint(B)}")


print(f" THE A UNION B : {A.union(B)}")
print(f"THE B UNION A  {B.union(A)}")

print(f"THE SYMMETRIC DIFF : {A.symmetric_difference(B)}")

del A,B

