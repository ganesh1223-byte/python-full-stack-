'''greedy approach
backtracking
tail recursion
nested rcursion'''


#greedy approach

coins = list(map(int, input("enter coins: ").split()))
amount=int(input("enter a amount"))
total_count=0
for coin in coins:
    count=amount//coin
    if count>0:
        print(coin,"rupees:",count)
        total_count+=count
        amount%=coin
print("total coins:",total_count)


#backtracking

n=int(input("enter n:"))
def backtrack(s):
    if len(s)==n:
        print(s)
        return
    backtrack(s+"0")
    backtrack(s+"1") 


              
    

#tail recursion
def num(n):
    if n==0:
        return
    num(n-1)
    print(n, end="")
n=int(input("enter n:"))
num (n)




#nested recursion
def func(n):
    if n>10:
        return n
    return  (func(func(n+2)))
n=int(input("enter a num"))
print(func(n))





    
