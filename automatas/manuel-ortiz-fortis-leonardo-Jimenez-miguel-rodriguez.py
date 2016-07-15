//leonardo ismael valle jimenez
//manuel ortiz fortiz
//miguel rodriguez

mensaje = "ingrese los arreglos"
print mensaje

t = raw_input()
lista = []
for i in range(0, int(t)):
	lista.append(raw_input("Ingrese elemento -> "))

print "A^0 = E"
#---------------------------------------------------------------
a = "{"
for i in range(0, len(lista)):
	a = a + lista[i]+","
a = a + "}"
print "A^1 = "+a
#---------------------------------------------------------------
b = "{"
for i in range(0, len(lista)):
	for j in range(0, len(lista)):	
		b = b + lista[i]+lista[j]+","
b = b + "}"
print "A^2 = "+b
#---------------------------------------------------------------
c = "{"
for i in range(0, len(lista)):
	for j in range(0, len(lista)):	
		for k in range(0, len(lista)):
			c = c + lista[i]+lista[j]+lista[k]+","
c = c + "}"
print "A^3 = "+c
#---------------------------------------------------------------
d = "{"
for i in range(0, len(lista)):
	for j in range(0, len(lista)):	
		for k in range(0, len(lista)):
			for l in range(0, len(lista)):
			d = d + lista[i]+lista[j]+lista[k]+lista[l]+","
#------------------------------------------------------------------
e = "{"
for i in range(0, len(lista)):
	for j in range(0, len(lista)):	
		for k in range(0, len(lista)):
                        for l in range(0, len(lista)):
                                for m in range(0, len(lista)):
			e = e + lista[i]+lista[j]+lista[k]+lista[m]+","
e = e + "}"
print "A^5 = "+e
#---------------------------------------------------------------
f = "{"
for i in range(0, len(lista)):
	for j in range(0, len(lista)):	
		for k in range(0, len(lista)):
                        for l in range(0, len(lista)):
                                for m in range(0, len(lista)):
                                        for n  in range(0, len(lista)):
			e = e + lista[i]+lista[j]+lista[k]+lista[m]+lista[m]+","
f = f + "}"
print "A^ = "+f
#---------------------------------------------------------------

			

			
a = len(d)
d[a-2].replace(",","}")
#d = d + "}"
print "A^4 = "+d
#print "------------------------------"
#print len(cadena)
#for i in range(0, 10,2):

