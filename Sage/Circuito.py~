# -*- coding: utf-8 -*-

from sage.all import * # importar tudo do sage

def construirT(listaRaizes):
	x = var('x')
	t = 0
	t = prod((x - ri) for ri in listaRaizes)
	return t


def construirConjPolinomios(ops,V,W,Y,nRaizes):
	contaRaiz = 0 #diz-nos qual gate de mutiplicacao (raiz) estamos
	contaOps = 0 # conta operaçoes de input e multiplicacao, indica em qual indice dos vetores V,W e Y os polinomios relativos a cada input e mutiplicacao devem ser colocados

	#
	for i in range(0,len(ops)):
		if ops[i].split(' ', 1)[0] == "input":
			###    Y
			aux = []
			for j in range (0,nRaizes):
				aux.append((j+1,0))

			Y[contaOps] = P.lagrange_polynomial(aux)
			###   fim Y	

			contaOps += 1

		elif ops[i].split(' ', 1)[0] == "mult":
			contaRaiz += 1 # diz em que gate mutiplicacao estamos,os polinomios tem que ter valor 1 nesta raiz e zero nas outras
			
			###   V
			aux = []
			indiceEsq = int(ops[i].split(' ', 3)[1])
			if ops[indiceEsq -1].split(' ', 1)[0] == "input":
				for j in range (0,nRaizes):
					if j+1 == contaRaiz:
						aux.append((contaRaiz,1))
					else:
						aux.append((j+1,0))
				V[indiceEsq - 1] = P.lagrange_polynomial(aux)
			elif ops[indiceEsq - 1].split(' ', 1)[0] == "mult":
				nAdds = int(ops[indiceEsq - 1].split(' ', 3)[3])# n de "add" antes desta mult		
				for j in range (0,nRaizes):
					if j+1 == contaRaiz:
						aux.append((contaRaiz,1))
					else:
						aux.append((j+1,0))
				V[indiceEsq - 1 - nAdds] = P.lagrange_polynomial(aux)
			elif ops[indiceEsq - 1].split(' ', 1)[0] == "add":
				stack = []
				nItems = 0

				stack.append(int(ops[indiceEsq - 1].split(' ', 2)[1]))
				stack.append(int(ops[indiceEsq - 1].split(' ', 2)[2]))
				nItems += 2

				while nItems > 0:
					k = stack[nItems-1] # k (elemento no topo da stack) é o indice do vetor ops que vamos analisar se é mult,add ou input
					nItems -= 1
					
					aux = []
					if ops[k-1].split(' ', 1)[0] == "input":
						for j in range (0,nRaizes):
							if j+1 == contaRaiz:
								aux.append((contaRaiz,1))
							else:
								aux.append((j+1,0))
						V[k-1] = P.lagrange_polynomial(aux)
					elif ops[k-1].split(' ', 1)[0] == "mult":
						nAdds = int(ops[k - 1].split(' ', 3)[3])# n de "add" antes desta mult		
						for j in range (0,nRaizes):
							if j+1 == contaRaiz:
								aux.append((contaRaiz,1))
							else:
								aux.append((j+1,0))
						V[k - 1 - nAdds] = P.lagrange_polynomial(aux)
					elif ops[k-1].split(' ', 1)[0] == "add":
						stack.append(int(ops[k - 1].split(' ', 2)[1]))
						stack.append(int(ops[k - 1].split(' ', 2)[2]))
						nItems += 2
									
			###   fim V

			###   W
			aux = []
			indiceDir = int(ops[i].split(' ', 3)[2])
			if ops[indiceDir - 1].split(' ', 1)[0] == "input":
				for j in range (0,nRaizes):
					if j+1 == contaRaiz:
						aux.append((contaRaiz,1))
					else:
						aux.append((j+1,0))
				W[indiceDir - 1] = P.lagrange_polynomial(aux)
			elif ops[indiceDir - 1].split(' ', 1)[0] == "mult":
				nAdds = int(ops[indiceDir - 1].split(' ', 3)[3])# n de "add" antes desta mult		
				for j in range (0,nRaizes):
					if j+1 == contaRaiz:
						aux.append((contaRaiz,1))
					else:
						aux.append((j+1,0))
				W[indiceDir - 1 - nAdds] = P.lagrange_polynomial(aux)
			elif ops[indiceDir - 1].split(' ', 1)[0] == "add":
				stack = []
				nItems = 0

				stack.append(int(ops[indiceDir - 1].split(' ', 2)[1]))
				stack.append(int(ops[indiceDir - 1].split(' ', 2)[2]))
				nItems += 2

				while nItems > 0:
					k = stack[nItems-1] # k (elemento no topo da stack) é o indice do vetor ops que vamos analisar se é mult,add ou input
					nItems -= 1
					
					aux = []
					if ops[k-1].split(' ', 1)[0] == "input":
						for j in range (0,nRaizes):
							if j+1 == contaRaiz:
								aux.append((contaRaiz,1))
							else:
								aux.append((j+1,0))
						W[k-1] = P.lagrange_polynomial(aux)
					elif ops[k-1].split(' ', 1)[0] == "mult":
						nAdds = int(ops[k - 1].split(' ', 3)[3])# n de "add" antes desta mult		
						for j in range (0,nRaizes):
							if j+1 == contaRaiz:
								aux.append((contaRaiz,1))
							else:
								aux.append((j+1,0))
						W[k - 1 - nAdds] = P.lagrange_polynomial(aux)
					elif ops[k-1].split(' ', 1)[0] == "add":
						stack.append(int(ops[k - 1].split(' ', 2)[1]))
						stack.append(int(ops[k - 1].split(' ', 2)[2]))
						nItems += 2
			###   fim W
						
			###   Y
			aux = []
			for j in range (0,nRaizes):
				if j+1 == contaRaiz:
					aux.append((contaRaiz,1))
				else:
					aux.append((j+1,0))

			Y[contaOps] = P.lagrange_polynomial(aux)
			###  fim Y

			contaOps += 1

	#no V,W e Y os indicies que tiverem o valor "#" será adicionado lá o polinomio 0
	#um indice nos vetors de polinomios ter o valor "#" siginica que nesse indice a operaçao nao é esquerda,direita ou resultado de uma mult (raiz)
	for i in range(0,len(V)):
		if V[i] == '#':
			V[i] = 0
		if W[i] == '#':
			W[i] = 0

	return V,W,Y



#conjunto de polinomios
V = []
W = []
Y = []


Zn = IntegerModRing(111)
P = PolynomialRing(QQ, 'x') 

condicao = True # condicao do ciclo que vai receber as linhas de texto do ficheiro
outPut = None # se no fim outPut for None então algo correu mal ou entao nao foi encontrada a operacao output

ops = [] # vetor que guarda as operaçoes vindas do ficheiro (operaçoes são: input x,add x y,mult x y)
valores = [] # valores de todas as operacoes
C = [] # valores dos inputs e dos resultados das multiplicacoes, ira ser usado na construcaao do polinomio p
nRaizes = 0
contaAdd = 0

try:
	strLida = raw_input()
	while condicao :
		# [0] = "input"            [1] = valor do input
		if strLida.split(' ', 1)[0] == "input":
			ops.append(strLida)
			# vai buscar o valor do input e passa para inteiro
			valores.append(int(strLida.split(' ', 1)[1]))
			C.append(int(strLida.split(' ', 1)[1]))

			# colocamos '#' para ir preenchendo as posicoes dos vetores para mais tarde poder usar os indices desses vetores e colocar lá o respectivo polinomio 
			V.append('#')
			W.append('#')
			Y.append('#')

			strLida = raw_input()
			
		elif strLida.split(' ', 1)[0] == "add":
			ops.append(strLida)
			# (ex "add 1 2" soma o que esta na posicao 0 com o da posicao 1 do vetor valores e faz o correspontende modulo) 
			contaAdd += 1
			valores.append(Zn(valores[int(strLida.split(' ', 2)[1]) -1] + valores[int(strLida.split(' ', 2)[2]) -1]))
			strLida = raw_input()
			
		elif strLida.split(' ', 1)[0] == "mult":
			#concatena a string lida do ficheiro com o numero de operaçoes "add" antes desta operacao "mult"
			ops.append( strLida + " " + str(contaAdd))
			nRaizes += 1 
			# (ex "mult 1 2" mutiplica o que esta na posicao 0 com o da posicao 1 do vetor valores e faz o correspontende modulo) 
			valores.append(Zn(valores[int(strLida.split(' ', 2)[1]) -1] * valores[int(strLida.split(' ', 2)[2]) -1]))
			C.append(Zn(valores[int(strLida.split(' ', 2)[1]) -1] * valores[int(strLida.split(' ', 2)[2]) -1]))

			V.append('#')
			W.append('#')
			Y.append('#')

			strLida = raw_input()
			
		elif strLida.split(' ', 1)[0] == "output":
			ops.append(strLida)
			outPut = valores[int(strLida.split(' ', 2)[1]) -1]
			condicao = False
		else:
			print "Operacao nao conhecida (operacao recebida do ficheiro nao e input,add, ou mult)"
			condicao = False
except EOFError:
	pass # se der esta exepçao EOF ele vai continuar e ignorar


#contruir a lista de raizes, caso tenha 2 raizes por exemplo esta lista tera os elementos [1,2],servira para contruir o polinomio t
listaRaizes = []
for i in range(0,nRaizes):
	listaRaizes.append(i+1)

t = construirT(listaRaizes)

V,W,Y = construirConjPolinomios(ops,V,W,Y,nRaizes)

resV = 0
resW = 0
resY = 0

for i in range(0,len(V)):
	resV += ZZ(C[i]) * V[i]	
	resW += ZZ(C[i]) * W[i]
	resY += ZZ(C[i]) * Y[i]

p = resV * resW - resY

# p%t se der zero entao t divide p
print p % t






