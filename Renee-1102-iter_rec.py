'''
Pseudo Code 
Define base and exponent inside iterative power 
Set base to be either interger or float value 
Set exponent to only interger value bigger or equal to 0
Return the value of base with the exponent in either interger form of float form
'''

base = float(input("base: "))
exp = int(input("exp: "))

def iterative_power(base, exp): 
    for i in range(exp):
        i = base * exp
    return i

print(iterative_power(base, exp))


'''
Pseudo Code 
Define base and exponent inside recursive power 
Set base to be either interger or float value 
Set exponent to only interger value bigger or equal to 0
Return the value of base with the exponent in either interger form of float form
'''

def recursive_power(base, exp):
    if exp >=0:
        n = base * exp 
        return n 

print(recursive_power(base, exp))
