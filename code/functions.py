
def hello_fn():
   return 'Hello'

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)

print(hello_fn())

print(fact(5))

def swap(a,b):
    var1 = a
    a = b
    b = var1
    return a,b


print(swap(4,5))
print(type(swap(4,5)))

