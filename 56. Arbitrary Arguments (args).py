
# *args = tuple

def add(*agrs):
    
    print(agrs)
    print(agrs[0] + agrs[1]) 
    
   
    sum = 0
    for item in agrs:
        sum += item
    print(sum)
     
    
    sum2 = 0
    for i in range(len(agrs)):
        sum2 += agrs[i]
    print(sum2)
  

add(10, 20, 30, 40)