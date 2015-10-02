input = open("int_data.txt") 
counts = [] 
c = list(map(int,input.split(" "))) 
for i in range(max(c)+1): 
    counts.append(c.count(c[i])) 
    #1
    print(i,' = ',c.count(c[i])) 
#2
print (counts.index(max(counts))) 
print (counts.index(min(counts))) 
#3
print ((101-counts.count(0))) 
