#O(1)- costant time complexity space complexity=O(1)
'''n=int(input("enter a num"))
print(n+100)'''

#O(n)=linear time compleity
'''n=int(input("enter a num"))
for i in range(1, n+1):
    print(i, end=" ")
    '''


#O(n)=linear time compleity and linear space complexity -O(1)
'''n=int(input("enter a num"))
arr=[]
for i in range(n):
    num= int(input("enter a num  "))
    arr.append(num)
print("list",arr)'''

#O(n^2) quadratic timecomplexity
'''n=int(input("enter a num"))
num=1
for i in range(n):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()'''


#logarthemic tc

'''n=int(input("enter a num"))
while n>1:
    print(n)
    n//=2
print(1)'''

#explanation  
'''n=int(input("enter a num"))
for i in range(n):
    j=n
    while j>1:
        print("before",j)
        j//=2
        print("affter",j)
    print()
print("done")'''
        
# exact code
'''n=int(input("enter a num"))
for i in range(n):
    j=n
    while j>1:
        j//=2
print("done")'''


'''def count(n):
    if n==0:
        return 1
    return count(n-1) + count(n-1)
n=int(input("enter a num"))
print("result:",count(n))'''


        
