import operator
from fractions import Fraction

class stuple(tuple):
    def __add__(self, other):
        return self.__class__(map(operator.add, self, other))

def Somar(a,b):
    a = list(a)
    b = list(b)
    tupla1 = stuple(a)
    tupla2 = stuple(b)
    return (tupla1+tupla2)

def Subtrair(a,b):
    a = list(a)
    b = list(b)
    tupla1 = stuple(a)
    tupla2 = stuple(b)
    tupla2 = Multiplicar(-1, tupla2)
    return (tupla1+tupla2)

def ProdutoInterno(u,v):
	resultado = 0
	for x in range(len(u)):
		resultado += u[x]*v[x]
	return resultado

def Multiplicar(r,t):
    resultado = [0]*len(t)
    for x in range(len(t)):
        resultado[x] = r*(t[x]) 
    return tuple(resultado)

def BaseOrtogonal(u):
    v = [0]*len(u)
    t = [0]*len(u)
    v[0] = u[0]
    t[0] = u[0]
    for x in range(len(u)-1):
            vnumber = 0
            vprovisorio = (0,)*len(u[0])
            while (vnumber<=x):
                ie = (ProdutoInterno(u[x+1],v[vnumber]))/(ProdutoInterno(v[vnumber],v[vnumber]))
                vprovisorio = Somar(vprovisorio, Multiplicar(ie,v[vnumber]))
                vnumber+=1
            v[x+1] = Subtrair(u[x+1],vprovisorio)
            conversao = list(v[x+1])
            for p in range(len(conversao)):
                conversao[p] = str(Fraction(conversao[p]).limit_denominator())
            t[x+1] = tuple(conversao)
    print("Orthogonal bases:", t)
    return t

counter = 0
vector = []
insert = (0,)
print ("Type 'go' when you're done.")
while insert != ["g","o"]:
    counter += 1
    insert = list(input("Enter vector number %d: " % (counter)))
    if insert != ["g","o"]:
        while "," in insert:
            insert.remove(",")
        while " " in insert:
            insert.remove(" ")
        while "/" in insert: #Converts fractions from input to floats
            position = insert.index("/")
            prior = float(insert[position-1])
            latter = float(insert[position+1])
            insert[position-1] = prior/latter
            insert.pop(position)
            insert.pop(position)
        for x in range(len(insert)):
            insert[x] = float(insert[x])
        vector.append(tuple(insert))
        print("\n")
        print("Current vector space: ", vector)
print("\n")
BaseOrtogonal(vector)
