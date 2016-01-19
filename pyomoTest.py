from __future__ import division 
import pyomo
from pyomo.environ import * 

p = AbstractModel()

p.m = Param(within=NonNegativeIntegers)
p.n = Param(within=NonNegativeIntegers)

p.I = Set()
p.J = Set()

p.a = Param(p.I, p.J)
p.b = Param(p.I)
p.c = Param(p.J)

p.x = Var(p.J, domain=NonNegativeReals)
def obj_function(p):
	return summation(p.c, p.a)

p.OBJ = Objective(rule=obj_function, sense=maximize)
def const_expression(p, i):
	return sum(p.a[i,j] * p.x[j] for i in p.J) <= p.b[i]

p.AxbConstraint = Constraint(p.I, rule=const_expression)
