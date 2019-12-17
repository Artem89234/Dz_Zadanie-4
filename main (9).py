s1 = ['Write', 'Black', 'Red']
s2 = ['Red', 'Green']
a = len(s1)
b = len(s2)
k = b
t = []
for i in range(a):
    k = b
    for j in range(b):
        if s1[i] != s2[j]:
            k = k - 1
    if k == 0:
        t.append(s1[i])
        
print(t)
    