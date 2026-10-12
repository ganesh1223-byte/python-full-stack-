#direct recursion:

'''def number(n):
    if n==0:
        return
    print(n)
    number(n-1)
n=int(input("enter n "))
number(n)'''


'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter a number:"))
print("factorial:",fact(n))'''
    



#indirect recurssion

'''def one(n):
    if n<=0: 
        return
    print("one:",n)
    two(n-1)
def two(n):
    if n<=0:
        return
    print("two:",n)
    one(n-1)
n=int(input("enter a number :"))
one(n)
'''

#indirect recurssion in even and odd numbers finding ,"imp q in mahendra tech".
'''def even(n):
    if n==0:
        print(copy,"is even")
        
        return
            
    odd(n-1)
def odd(n):
    if n==0:
        print(copy,"is odd")
        return
    even(n-1)
n=int(input("enter a number:"))
copy = n
even(n)'''


#tree recurssion



def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    fun(n-1)
n=int(input("enter  the number:"))
fun(n)
