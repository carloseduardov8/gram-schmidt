import operator

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
    v[0] = u[0]
    for x in range(len(u)-1):
            vnumber = 0
            vprovisorio = (0,)*len(u[0])
            while (vnumber<=x):
                ie = (ProdutoInterno(u[x+1],v[vnumber]))/(ProdutoInterno(v[vnumber],v[vnumber]))
                vprovisorio = Somar(vprovisorio, Multiplicar(ie,v[vnumber]))
                vnumber+=1
            v[x+1] = Subtrair(u[x+1],vprovisorio)
    return v
