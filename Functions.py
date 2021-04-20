print("hello")
#lambda for multiple arguments 
x = lambda a,b: a+b
print(x(5,60))

def f1(n):
    return lambda a:a*n
double= f1(2)
triple=f1(3)
print(double(11))
print(triple(11))

#Filter function
def prime(x):
    for n in range(2,x):
        if x%n == 0:
            return False
        else:
            return True
filtered=filter(prime,range(10))#Filter function needs a function, sequence
print("prime numbers are", list(filtered))
#Map function
def square(x):
    return x*x
numb = [1,2,3,4,5,4]
listsquare=map(square,numb)
print(list(listsquare)) #map function is similar to filter function but doesnt need true or false
