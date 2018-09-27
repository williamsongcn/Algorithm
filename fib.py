'''a fib that can be runned quicklierx'''
x=0
def slowFib(n):
    global x
    x+=1
    if n==0 or n == 1:
        return 1
    else:
        
        return slowFib(n-1)+slowFib(n-2)
y=0
def fastFib(n,memo={}):
    global y
    y+=1
    if n==0 or n == 1:
        return 1
    try :
        return memo[n]
    except KeyError:
        result=fastFib(n-1,memo)+fastFib(n-2,memo)
        memo[n]=result
        return result
slowFib(20)
fastFib(120)
print('x=',x,'\n','y=',y)
