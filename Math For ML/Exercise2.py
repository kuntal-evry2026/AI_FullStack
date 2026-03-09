import sympy as sp

#define a function 

x = sp.Symbol('x')
f = x**3 -5*x + 7

#compute derivatives

derivatives = sp.diff(f,x)
print("Function :" ,f)
print("Derivative :" , derivatives)

#compute gradiant

y, z = sp.symbols('y z')

g = y**2 + 3*z**2 + 4*y*z

grad_y = sp.diff(g, y)
grad_z = sp.diff(g, z)

print("Partial derivatives:", grad_y, grad_z)


