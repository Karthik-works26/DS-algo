string1 = input("enter the string1") 
stirng2 = input("enter the string2") 
############## sorting the strings lexicographically 
def brute_force(string1,string2):
    return sorted(string1) == sorted(string2)  
##################### suboptimal solutions using two hashmaps 
from collections import defaultdict 
def optimal1(string1,string2):
    hashmap1 = defaultdict(int)  
    hashmap2 = defaultdict(int)
    for char in string1:
        hashmap1[char] += 1 
    for char in string2:
        hashmap2[char] +=1 
    for i in range(len(string1)):
        if hashmap1[i] != hashmap2[i]:
            return False 
    return True 
############## single map solutions 
def optimal2(stirng1,string2): 
    hashmap3 = defaultdict(int) 
    for char in string1:
        hashmap3[char] += 1 
    for char in string2:
        hashmap3[char] -= 1 
    for i in hashmap3.values():
        if i != 0:
            return False 
    return True 
