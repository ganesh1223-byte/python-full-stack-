#natural numbers
'''n=int(input("enter the n:"))
for i in range(1, n+1):
    if i%2==1:
        print(i, end=" ")'''
    

#star square pattern
'''n=int(input("enter the n:"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()'''


#print (i)--numbers
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(i, end=" ")
    print()'''
    
        
#print(j)--numbers
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        print(j, end=" ")
    print()   '''


#hallow squar pattern

'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()'''


#print X 
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or  i+j==n-1:
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()'''

#print hallow-square with X
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==j or  i+j==n-1 or i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()'''

#timer stand
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or  i+j==n-1:
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()'''



#butter fly 
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or  i+j==n-1:
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()'''


#plus(+)in hallow square
'''n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()
'''



n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==j or  i+j==n-1:
            print("*", end=" ")
        else:
            print(" " ,end=" ")
    print()
