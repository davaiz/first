#1
for i in range(0, len(A)-1 , 2):
    A[i], A[i + 1] = A[i + 1], A[i]
print(A)
#2
A.insert(0, A.pop())
print(A)
#3
for i in A:
    if A.count(i) == 1:
        print(i, end = ' ')
#4
k = None
for i in A:
    if k == None:
        k = A.count(i)
        h = i  
    elif A.count(i) > k:
        h = i
print(h)

    

