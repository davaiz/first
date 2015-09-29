#1
from random import *
output = open('int_data.txt', 'w')
for i in (10000000):
    print(randint(0, 100), file = output)
output.close()
#2
from random import *
output = open('float_data.txt', 'w')
for i in (10000000):
    print(randint(0, 100)//100, file = output)
output.close()  


    
