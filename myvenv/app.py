def hello():
    return "Hello, World!"

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b

def mod(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a%b