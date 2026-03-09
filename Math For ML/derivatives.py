import sympy as sp

x= sp.Symbol('x')
f=x**2
derivatives = sp.diff(f,x)

print("Derivatives" , derivatives)


#partial derivatives 

a,b  = sp.symbols('a b')
f = a**2 + b**2
grad_a= sp.diff(f,a)
grad_b= sp.diff(f,b)

print ("partial derivative" , grad_a ,grad_b)