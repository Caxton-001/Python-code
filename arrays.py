# Python Arrays
import array
from array import *
import sys

# Array of typecode i
scores= array('i',[12,15,20,50,34,65,70])
print(scores)

# Array of typecode f
score=array('f',[12.5,25.8,65.1,36.7,98.5,31.4])

newscore=array(score.typecode,[])

print(newscore)

# implementing a for loop whilst using arrays
newscores=array(scores.typecode,[])
for i in scores:
    newscores.append(i*2)
    i+=1

print(newscores)

# Getting the id of an array
the_id=id(scores)
id(scores)
id2=id(score)

print(id(scores))
print(id2)
print(the_id)

# Getting size of scores using sys module
size=sys.getsizeof(scores)
print(size)
