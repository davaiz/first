#1
input = open('float_data.txt' , 'r') 
A = input.readlines() 
for i in range(len(A)): 
    A[i] = float(A[i]) 
sr = sum(A)/len(A)
print(sr)  
#2
input = open('float_data.txt' , 'r') 
A = input.readlines() 
for i in range(len(A)): 
    A[i] = float(A[i]) 
sr = sum(A)/len(A) 
smq = 0 
for i in range(len(A) 
    smq += A[i] ** 2: 
srkvr = (smq/len(A) - sr**2)**0.5 
print(srkvr)
#3
input = open('float_data.txt' , 'r')
mmax = None 
mmin = None 
c = list(map(float,(input.split(' '))))
for i in range(len(c)): 
    if mmax == None: 
        mmax = ch[i] 
        mmin = ch[i] 
    else: 
        mmax = max(ch[i],maxx) 
        mmin = min(ch[i],minn) 
print(mmax, c.index(mmax), mmin, c.index(mmin))

